from bs4 import BeautifulSoup
from wiki_search import WikiSearch


class TextObject:
    def __init__(self, text, wiki):
        self.__text = text
        self.wiki = wiki # WikiSearch type

    @property
    def text(self):
        return self.__text
    
    @text.setter
    def text(self, value):
        self.__text = value

    @property
    def wiki(self):
        return self.__wiki
    
    @wiki.setter
    def wiki(self, value):
        if type(value) is WikiSearch:
            self.__wiki = value
        else:
            raise ValueError("The value is not a WikiSearch object")

    @property
    def part(self):
        return self.__part
    
    @part.setter
    def part(self, value):
        self.__part = value

    def clear_text(self):
        soup = BeautifulSoup(self.text, 'html.parser')
        self.text = soup.get_text()
