from title_module import Title
from year_list import YearList
from year_data import YearData

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

    def find_years(self):
        n_digites = 0
        year_start, year_end = 0, 0
        year = ""
        for i in range(0, len(self.__text)):
            c = self.__text[i]
            if c.isnumeric():
                if n_digites > 4:
                    n_digites = 0
                    year = ""
                    continue
                if n_digites == 0:
                    year_start = i
                n_digites += 1
                year += c
            else:
                if n_digites > 0 and n_digites <= 4:
                    year_end = i - 1
                    try:
                        year = int(year)

                        distance = self.calculate_distance(year_start, year_end)

                        year_data = YearData(year, year_start, year_end, distance)
                        self.__year_list.add_year(year_data)
                    except:
                        raise TypeError("could not parse, year is not a number")
                n_digites = 0
                year = ""
        return self.__year_list

    def calculate_distance(self, year_start, year_end):
        closest = min(self.__title_locations, key=lambda x: min(abs(x - year_start), abs(x - year_end)))

        return min(abs(closest - year_start), abs(closest - year_end))

    def __str__(self):
        text = "TextPart:\n"
        text_beginning = "\ttext: " + self.text[list(self.titles)[0].start-10: list(self.titles)[0].end+10] + "..."
        text_beginning  = text_beginning.replace("\n", " ")
        text += text_beginning
        text += "\n\tTitles: " + str(len(self.titles))
        return text