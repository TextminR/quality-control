from bs4 import BeautifulSoup
import requests
import wikipedia

class WikiSearch:
    def __init__(self, book):
        self.book = book
        # dictionary to store the found content: found[search + lang] = content
        self.found = {}
        search = wikipedia.search(book.author)
        search += wikipedia.search(book.title)

    def gethtml(self, lang = "de"):
        # replace the spaces with the _ so it can be used in the url
        author = self.book.author
        author.replace(" ", "_")
        response = requests.get(
            url="https://" + lang + ".wikipedia.org/wiki/" + author,
        )
        # get the content of the website
        soup = BeautifulSoup(response.content, 'html.parser')
        content = soup.find(id="content").__str__()
        return content
    
    # checks if a part of the title is in the content, if so return True
    def find_title(self, content):
        for p in self.title.split(" "):
            # check if a part of the title is in the content of the website
            if p in content:
                return True
                # print the deatils of the search
                # print("Search: " + s + "\nWord in Text: " + p)

    # search one of the search words
    def search_each(self, search, lang = "de"):
        content = WikiSearch.gethtml(search, lang)
        if WikiSearch.find_title(content):
            # add the content to the found list
            self.found[search + lang] = content

    def search_all(self):
        for s in self.search:
            lang = ["de", "en"]
            self.search_each(s, lang[0])
            self.search_each(s, lang[1])

            