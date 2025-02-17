from static import Static
import re
import wikipedia
import requests
from bs4 import BeautifulSoup

class Bookdata:
    def __init__(self, author, title, odl_date, lang=None, birth=None, death=None):
        self.__author = author
        self.__title = title
        self.title_clean = title
        if lang is None:
            self.__lang = "de"
        else:
            self.__lang = lang
        try: self.__old_date = int(odl_date)
        except: raise TypeError("could not parse, old_date is not a number")
        self.__birth = birth
        self.__death = death
        if birth is None or death is None:
            self.get_years()
        self.title_parts = self.__title_clean

    # author
    @property
    def author(self):
        return self.__author

    @author.setter
    def author(self, value):
        self.__author = value.replace(",", "")

    # title
    @property
    def title(self):
        return self.__title

    @title.setter
    def title(self, value):
        self.__title = value

    # title_clean
    @property
    def title_clean(self):
        return self.__title_clean

    @title_clean.setter
    def title_clean(self, value):
        # the original book title is copied, only letters
        split_title = re.sub(r'[^a-zA-Z0-9\s]', '', value) # value should be same as self.title
        # the newly selected title will be split in single words
        split_title = split_title.split()
        words = None
        # the unimportant words will be removed
        words = Static.get_words()
        split_title = [word for word in split_title if word.lower() not in words]
        # print(split_title)
        title_clean = " ".join(split_title)
        self.__title_clean = title_clean

    # title_parts
    @property
    def title_parts(self):
        return self.__title_parts

    @title_parts.setter
    def title_parts(self, value):
        parts = value.split(" ")
        for p in parts:
            value = Bookdata.replace(value, p, "ss", "ß")
            value = Bookdata.replace(value, p, "ß", "ss")
            value = Bookdata.replace(value, p, "ö", "oe")
            value = Bookdata.replace(value, p, "ü", "ue")
            value = Bookdata.replace(value, p, "ä", "ae")
            value = Bookdata.replace(value, p, "ae", "ä")
            value = Bookdata.replace(value, p, "ue", "ü")
            value = Bookdata.replace(value, p, "oe", "ö")
        self.__title_parts = value

    @staticmethod
    def replace(value, part, old, new):
        temp = part.replace(old, new)
        if temp == part:
            return value
        else:
            return value + " " + temp

    # odl_date
    @property
    def old_date(self):
        return self.__old_date

    @old_date.setter
    def old_date(self, value):
        self.__old_date = value

    # birth
    @property
    def birth(self):
        return self.__birth

    @birth.setter
    def birth(self, value):
        self.__birth = value

    # death
    @property
    def death(self):
        return self.__death

    @death.setter
    def death(self, value):
        self.__death = value
    
    def get_years(self):
        lang = self.__lang
        wikipedia.set_lang(lang)
        search = wikipedia.search(self.author)
        # print(search)
        for s in search:
            site = self.get_site(s, lang)[0:600]
            if self.extract_brackets(site):
                return True
        if self.__lang == "de":
            lang = "en"
        elif self.__lang == "en":
            lang = "de"
        wikipedia.set_lang(lang)
        search = wikipedia.search(self.author)
        # print(search)
        for s in search:
            site = self.get_site(s, lang)[0:1000]
            if self.extract_brackets(site):
                return True
        self.__birth = self.__old_date - 50
        self.__death = self.__old_date + 50
        return False
    
    def extract_brackets(self, text) -> bool:
        array = []
        start = 0
        for n in range(0, len(text)):
            c = text[n]
            if c == "(":
                start = n
                continue
            if c == ")":
                end = n
                temp = text[start:end+1]
                array.append(temp)
                if self.extract_years(temp):
                    return True
        return False

    def extract_years(self, text) -> bool:
        x = 0
        years = set()
        year = ""
        for n in range(0, len(text)):
            c = text[n]
            if bool(re.fullmatch(r"[0-9]+", c)) and x < 4:
                x += 1
                year += c
            else:
                if x > 0 and x <= 4:
                    try:
                        year = int(year)
                        years.add(year)
                    except:
                        raise TypeError("could not parse, year is not a number")
                x = 0
                year = ""
        if years is None or len(years) < 2:
            return False
        y1 = max(years)
        years.remove(y1)
        y2 = max(years)
        if not self.__old_date == None and not y2 == self.__old_date:
            return False
        self.__death = y1
        self.__birth = y2
        return True

    # get the site using one of the saved titles
    def get_site(self, search, lang = "de"):
        # replace the spaces with the _ so it can be used in the url
        search.replace(" ", "_")
        response = requests.get(
            url="https://" + lang + ".wikipedia.org/wiki/" + search,
        )
        # get the content of the website
        soup = BeautifulSoup(response.content, 'html.parser')
        content = soup.find(id="content").__str__()

        soup = BeautifulSoup(content, 'html.parser')
        content = soup.get_text()

        return content

    
    # Keller, Helen [1880-1968]: "die geschichte meines lebens" (1880)
    def __str__(self) -> str:
        text = f"{self.__author} [{self.__birth}-{self.__death}]"
        text += ": \"" + self.__title + "\"" + " (" + str(self.__old_date) + ")" 
        return text


if __name__ == "__main__":
    book = Bookdata("Keller, Helen", "di.e: ,Das Ge,schichte: meines lebens", 1880, 1880, 1968)
    print(book)
    print(book.title_clean)
