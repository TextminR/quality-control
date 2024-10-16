from bookdata import Bookdata
from wiki_search import WikiSearch


if __name__ == "__main__":
    book = Bookdata("Kleist, Heinrich von", "Ausgewählte Schriften", 1777, 1777, 1811)
    w = WikiSearch(book)
    # takes a new Wikipedia site and saves it
    w.next_search()
    # clears the saved text of any html tags
    w.textobjects[0].clear_text()
    # finds the title of the book in the text and creates a TextPart object and removes the part with the title from the original text
    if w.textobjects[0].find_title(book.title_clean):
        print("True")
        print(w.textobjects[0])
        print(w.textobjects[0].part[0])
        print("Number of Titles in the part: " + str(w.textobjects[0].part[0].find_all_titles(book.title_clean)))
        year_list = w.textobjects[0].part[0].find_years()
        print(year_list.__str__())
        year_list.clear_years(book.birth, book.death)
        print(book.birth, book.death)
        print(year_list.__str__())
    else:
        print("False")

