from static import Static
import re

class Bookdata:
    def __init__(self, author, title, odl_date, birth, death):
        self.author = author
        self.title = title
        self.set_title_clean()
        self.old_date = odl_date
        self.birth = birth
        self.death = death

    def set_author(self, author):
        self.author = author.replace(",", "")
    
    def set_title(self, title):
        self.title = title

    def set_author(self, author):
        self.author = author
    
    def set_title(self, title):
        self.title = title
    
    def set_title_clean(self):
        split_title = re.sub(r'[^a-zA-Z0-9\s]', '', self.title)
        split_title = split_title.split()
        words = Static.words
        split_title = [wort for wort in split_title if wort.lower().strip(",.!?") not in words]
        title_clean = " ".join(split_title)
        self.title_clean = title_clean
    
    def set_old_date(self, old_date):
        self.old_date = old_date
    
    def set_birth(self, birth):
        self.birth = birth
    
    def set_death(self, death):
        self.death = death

    # Keller, Helen [1880-1968]: "die geschichte meines lebens" (1880)
    def __str__(self) -> str:
        text = self.author + " [" + str(self.birth) + "-" + str(self.death) + "]"
        text += ": \"" + self.title + "\"" + " (" + str(self.old_date) + ")" 
        return text


if __name__ == "__main__":
    book = Bookdata("Keller, Helen", "die: Das Geschichte: meines lebens", 1880, 1880, 1968)
    print(book)
    print(book.title_clean)
