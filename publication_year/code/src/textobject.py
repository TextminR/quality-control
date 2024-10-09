from bs4 import BeautifulSoup
from bookdata import Bookdata
from title_module import Title
import textpart


class TextObject:
    def __init__(self, text):
        self.__text = text # original text
        self.__part = [] # Part[] type

    @property
    def text(self):
        return self.__text
    
    @text.setter
    def text(self, value):
        self.__text = value

    @property
    def part(self):
        return self.__part
    
    @part.setter
    def part(self, value):
        self.__part = value

    def clear_text(self):
        soup = BeautifulSoup(self.text, 'html.parser')
        self.text = soup.get_text()
    
    def find_title(self, title):
        for title_part in title.split(" "):
            n = self.text.find(title_part)
            if n != -1:
                title = Title(n, n + len(title_part))
                self.remove_part(title, title_part)
                return True
        return False
        
    def remove_part(self, title, word):
        margin = 250
        text_part = self.text[title.start - margin: title.end + margin]
        n = text_part.find(word)
        title = Title(n, n + len(word))
        self.__part.append(textpart.TextPart(text_part, title))
        self.text = self.text.replace(text_part, "")


    def __str__(self):
        text = "TextObject: \n"
        text_beginning = "\t" + self.text[:40] + "..."
        text_beginning  = text_beginning.replace("\n", " ")
        text += text_beginning
        text += "\n\tParts: " + str(len(self.part))
        return text

