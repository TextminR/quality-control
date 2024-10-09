from bs4 import BeautifulSoup
import requests
import wikipedia
from bookdata import Bookdata
import textobject

class WikiSearch:

    def __init__(self, book):
        self.__textobjects = [] # list of TextObject type
        self.book = book # Bookdata type
        self.get_tetles()

    # book
    @property
    def textobject(self):
        return self.__textobject

    @textobject.setter
    def textobject(self, value):
        self.__textobject = value

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

    # get the tieles of the wikipedia pages, using the author and the title of the book, with possible publication years
    def get_tetles(self):
        self.search = wikipedia.search(self.__book.author)
        self.search += wikipedia.search(self.__book.title)
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

        self.textobjects.append(textobject.TextObject(content))

        return content

    def next_search(self):
        if len(self.search) > 0:
            self.get_html(self.search.pop())
        else:
            return None

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
    
    # # checks if a part of the title is in the content, if so return True
    # def find_title(self, content):
    #     for p in self.title.split(" "):
    #         # check if a part of the title is in the content of the website
    #         if p in content:
    #             return True
    #             # print the deatils of the search
    #             # print("Search: " + s + "\nWord in Text: " + p)

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
        text = "WikiSearch:\n"
        text += "\tBook: " + self.__book.__str__()
        text += "\n\t" + "Number of wikipedia search titles: " + str(len(self.search))
        text += "\n\tTexts: " + str(len(self.textobjects))
        textobject = []
        for t in self.textobjects:
            textobject.append(t.__str__())
        for t in textobject:
            for i in t.split("\n"):
                if i == 0:
                    continue
                text += "\n\t" + i
        return text


if __name__ == "__main__":
    book = Bookdata("Keller, Helen", "die: Das Geschichte: meines lebens", 1880, 1880, 1968)
    w = WikiSearch(book)
    print(w)
    print(type(w.search))
    print(type(w.book))
    w.next_search()
    print(w)