from bs4 import BeautifulSoup
import requests
import wikipedia
from bookdata import Bookdata
from textobject import TextObject

class WikiSearch:
    def __init__(self, book):
        self.texts = [] # list of TextObject type
        self.book = book # Bookdata type
        self.get_tetles()

    # book
    @property
    def book(self):
        return self.__book

    @book.setter
    def book(self, value):
        if type(value) is Bookdata:
            self.__book = value
        else:
            raise ValueError("The value is not a Bookdata object")

    # search
    @property
    def search(self):
        return self.__search

    @search.setter
    def search(self, value):
        self.__search = value

    # found
    @property
    def found(self):
        return self.__found

    @found.setter
    def found(self, value):
        self.__found = value

    # get the tieles of the wikipedia pages, using the author and the title of the book, with possible publication years
    def get_tetles(self):
        self.search = wikipedia.search(book.author)
        self.search += wikipedia.search(book.title)
        self.search += ["milos", "milos"]
        self.__search = set(self.__search)

    # get the site using one of the saved titles
    def get_html(self, search, lang = "de"):
        # replace the spaces with the _ so it can be used in the url
        search.replace(" ", "_")
        response = requests.get(
            url="https://" + lang + ".wikipedia.org/wiki/" + search,
        )
        # get the content of the website
        soup = BeautifulSoup(response.content, 'html.parser')
        content = soup.find(id="content").__str__()

        self.texts.append(TextObject(search, self))

        return content

    # # get the site using one of the saved titles
    # def get_html(self, lang = "de"):
    #     # replace the spaces with the _ so it can be used in the url
    #     author = self.book.author
    #     author.replace(" ", "_")
    #     response = requests.get(
    #         url="https://" + lang + ".wikipedia.org/wiki/" + author,
    #     )
    #     # get the content of the website
    #     soup = BeautifulSoup(response.content, 'html.parser')
    #     content = soup.find(id="content").__str__()
    #     return content
    
    # checks if a part of the title is in the content, if so return True
    def find_title(self, content):
        for p in self.title.split(" "):
            # check if a part of the title is in the content of the website
            if p in content:
                return True
                # print the deatils of the search
                # print("Search: " + s + "\nWord in Text: " + p)

    # # search one of the search words
    # def search_each(self, search, lang = "de"):
    #     content = WikiSearch.gethtml(search, lang)
    #     if WikiSearch.find_title(content):
    #         # add the content to the found list
    #         self.found[search + lang] = content

    # def search_all(self):
    #     for s in self.search:
    #         lang = ["de", "en"]
    #         self.search_each(s, lang[0])
    #         self.search_each(s, lang[1])

    def __str__(self) -> str:
        text = self.__book.__str__()
        text += "\n"
        for s in self.__search:
            text += s + "; "
        return text


if __name__ == "__main__":
    book = Bookdata("Keller, Helen", "die: Das Geschichte: meines lebens", 1880, 1880, 1968)
    w = WikiSearch(book)
    print(w)
    print(type(w.search))