from static import Static
import re

class Bookdata:
    def __init__(self, author, title, odl_date, birth, death):
        self.__author = author
        self.__title = title
        self.title_clean = title
        self.__old_date = odl_date
        self.__birth = birth
        self.__death = death

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
        split_title = re.sub(r'[^a-zA-Z0-9\s]', '', self.title)
        split_title = split_title.split()
        words = Static.get_words()
        split_title = [wort for wort in split_title if wort.lower().strip(",.!?") not in words]
        title_clean = " ".join(split_title)
        self.__title_clean = title_clean

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
    
    # Keller, Helen [1880-1968]: "die geschichte meines lebens" (1880)
    def __str__(self) -> str:
        text = self.__author + " [" + str(self.__birth) + "-" + str(self.__death) + "]"
        text += ": \"" + self.__title + "\"" + " (" + str(self.__old_date) + ")" 
        return text


if __name__ == "__main__":
    book = Bookdata("Keller, Helen", "die: Das Geschichte: meines lebens", 1880, 1880, 1968)
    print(book)
    print(book.title_clean)
