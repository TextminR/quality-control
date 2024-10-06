from title_module import Title
import textobject

class TextPart:
    def __init__(self, textobject, text, title):
        self.textobject = textobject
        self.__text = text
        self.__titles = set()
        self.__titles.add(title)

    @property
    def textobject(self):
        return self.__textobject
    
    @textobject.setter
    def textobject(self, value):
        if type(value) is textobject.TextObject:
            self.__textobject = value
        else:
            raise ValueError("The value is not a TextObject object")

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

    # looks for all occurences of the title in the text
    def find_all_titles(self):
        for title_part in self.textobject.wiki.book.title_clean.split(" "):
            n = 0
            while True:
                n = self.text.find(title_part, n)
                if n == -1:
                    break
                title = Title(n, n + len(title_part))
                self.titles.add(title)
                n += len(title_part)
        return len(self.titles)

    def __str__(self):
        text = "TextPart: \n"
        text_beginning = "\t" + self.text[list(self.titles)[0].start-10: list(self.titles)[0].end+10] + "..."
        text_beginning  = text_beginning.replace("\n", " ")
        text += text_beginning
        text += "\n\tTitles: " + str(len(self.titles))
        return text