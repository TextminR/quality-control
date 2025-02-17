from title_module import Title
from year_list import YearList
from year_data import YearData
from extract import ExtractInterface
from manual import Manual

class TextPart:
    def __init__(self, text, title):
        self.__text = text
        self.__titles = set()
        self.__titles.add(title)
        self.__year_list = YearList()
        self.__title_locations = set()

    @property
    def text(self):
        return self.__text
    
    @text.setter
    def text(self, value):
        self.__text = value

    @property
    def titles(self):
        return self.__titles
    
    @titles.setter
    def titles(self, value):
        self.__titles = value

    def add_title(self, title):
        self.__titles.add(title)

    @property
    def year_list(self):
        return self.__year_list
    
    @year_list.setter
    def year_list(self, value):
        self.__year_list = value

    @property
    def title_locations(self):
        return self.__title_locations

    @title_locations.setter
    def title_locations(self, value):
        self.__title_locations = value
        pass

    @property
    def line_locations(self):
        return self.__line_locations

    @line_locations.setter
    def line_locations(self, value):
        self.__line_locations = value
        pass
    
    def calculate_locations(self):
        for t in self.titles:
            self.__title_locations.add(t.start)
            self.__title_locations.add(t.end)
        return self.__title_locations

    # looks for all occurences of the title in the text
    def find_all_titles(self, title):
        for title_part in title.split(" "):
            n = 0
            while True:
                n = self.text.find(title_part, n)
                if n == -1:
                    break
                title = Title(n, n + len(title_part))
                self.titles.add(title)
                n += len(title_part)
        self.calculate_locations()
        return len(self.titles)

    def find_years(self, extract: ExtractInterface = None):
        if extract == None:
            extract = Manual()
        self.year_list = extract.find_years(self.__text)
        self.calculate_distance()
        self.calculate_line_distance()
        return self.__year_list

    def calculate_distance(self):
        for year in self.__year_list.year_data:
            year_start = year.start
            year_end = year.end

            closest = min(self.__title_locations, key=lambda x: min(abs(x - year_start), abs(x - year_end)))

            year.distance = min(abs(closest - year_start), abs(closest - year_end))

    # calculates the number of line breaks between the year and the title
    def calculate_line_distance(self):
        self.find_lines()
        for year in self.__year_list.year_data:
            line_distance = 0

            # if title after year
            if year.end + year.distance in self.__title_locations:
                title_location = year.end + year.distance
                for l in self.__line_locations:
                    # if line is between year and title
                    if l > year.end and l < title_location:
                        line_distance += 1

            # if title befor year
            elif year.start - year.distance in self.__title_locations:
                title_location = year.start - year.distance
                for l in self.__line_locations:
                    # if line is between year and title
                    if l < year.start and l > title_location:
                        line_distance += 1

            year.line_distance = line_distance

    def find_lines(self):
        n = 0
        locations = set()
        while True:
            n = self.text.find("\n", n)
            if n == -1:
                break
            locations.add(n)
            n += 1
        self.__line_locations = locations

    def __str__(self):
        text = "TextPart:\n"
        text_beginning = "\ttext: " + self.text[list(self.titles)[0].start-10: list(self.titles)[0].end+10] + "..."
        text_beginning  = text_beginning.replace("\n", " ")
        text += text_beginning
        text += "\n\tTitles: " + str(len(self.titles))
        return text
