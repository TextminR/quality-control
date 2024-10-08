from bookdata import Bookdata
from wiki_search import WikiSearch


if __name__ == "__main__":
    book = Bookdata("Keller, Helen", "die: Das Geschichte: meines lebens", 1880, 1880, 1968)
    w = WikiSearch(book)
    # takes a new Wikipedia site and saves it
    w.next_search()
    # clears the saved text of any html tags
    w.texts[0].clear_text()
    # finds the title of the book in the text and creates a TextPart object and removes the part with the title from the original text
    if w.texts[0].find_title():
        print("True")
        print(w.texts[0])
        print(w.texts[0].part[0])
        print("Number of Titles in the part: " + str(w.texts[0].part[0].find_all_titles()))
    else:
        print("False")

