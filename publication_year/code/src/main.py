from copy import Error
from bookdata import Bookdata
from year_list import YearList
from wiki_search import WikiSearch
from db import DB
from static import Static
import time
from manual import Manual

# bookdata is {}
# book is Bookdata()
def next_book(bookdata, book):
    # book = Bookdata("Hesse, Hermann", "Umwege: Erzählungen", 1877, 1877 , 1962) # 1912
    # book = Bookdata("Droysen, Johann Gustav", "Geschichte Alexanders des Grossen", 1808, 1808, 1884) # 1833
    # book = Bookdata("Roda Roda", "500 Schwänke", 1872, 1872, 1945) # 1906
    # book = Bookdata("Humboldt, Wilhelm von", "Briefe an eine Freundin", 1767, 1767, 1835) # 1921

    book_start = str(bookdata["_source"]["text"][0])[:1000]
    # print(book_start)
    m = Manual()
    liste = m.find_years(book_start)
    liste.clear_years(book.birth, book.death)
    # print(liste)
    best_year = liste.find_best_year()
    # print(best_year)
    if best_year is not None:
        return best_year

    # print(book.title_parts)
    # correct_year = 1921 
    w = WikiSearch(book)
    year_list = YearList()
    loop = True
    empty = 0
    textobject_n = 0
    textpart_n = 0
    # text_with_correct_year = []
    # print("Search length: ", len(w.search))
    while loop:
        # takes a new Wikipedia site and saves it
        if not w.next_search():
            # print("No more searches")
            loop = False
            break
        textobject_n += 1
        # select the last saved text
        textobject = w.get_last_text()
        # clears the saved text of any html tags
        textobject.clear_text()
        parts = True
        while parts:
            # finds the title of the book in the text and creates a TextPart object and removes the part with the title from the original text
            if textobject.find_title_part(book.title_parts):
                # at least one part found in this search
                textpart_n += 1
                empty = 0

                p = textobject.get_last_part()
                # print("Number of Titles in the part: " + str(p.find_all_titles(book.title_parts)))
                new_years = p.find_years()
                new_years.clear_years(book.birth, book.death)
                year_list.combine_year_data(new_years)
                if not (new_years is None or len(new_years.year_data) == 0):
                    best_year = year_list.find_best_year()
                    if best_year is not None and best_year.score > 0.99:
                        return best_year
                    # if best_year == correct_year:
                    #     parts = False
                    #     loop = False
                    # if new_years.contains(correct_year):
                    #     text_with_correct_year.append(p.text)
            else:
                # print("No (more) Titles in this Search")
                empty += 1
                parts = False
                # if empty > 10:
                #     loop = False

    # print()
    # print("Done:")
    # print(year_list.__str__())
    best_year = year_list.find_best_year()
    # print("best_year:", best_year)

    # print("Textobjects: ", textobject_n, "Textparts: ", textpart_n)

    # for t in text_with_correct_year:
    #     print("p:")
    #     print(t)

    return best_year

if __name__ == "__main__":
    db = DB()

    index = Static.get_index()
    if index == None:
        raise Exception("No index found")

    for i in index:
        try:
            start = time.time()

            bookdata = db.get_bookdata(i)

            if not db.check_book(bookdata):
                print(i, "bad book data")
                continue

            book = Bookdata(bookdata["_source"]["author"], bookdata["_source"]["title"], bookdata["_source"]["year"])
            print(i, book)

            best_year = next_book(bookdata, book)

            print("Time in seconds: ", (time.time() - start))
            print("Year: ", best_year)
            if best_year is not None and book.old_date != best_year.year:
                if db.update_year(i, int(best_year.year)):
                    print("updated")
                else:
                    print("update failed")
            else:
                print("no update")
        except KeyboardInterrupt:
            raise KeyboardInterrupt
        except Exception as err:
            print(f"Error {err=}, {type(err)=}")
            continue



