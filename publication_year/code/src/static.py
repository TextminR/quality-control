import os

wd = os.path.dirname(__file__)
class Static:
    __words = None

    # Class method to get the class attribute
    @classmethod
    def get_words(cls):
        if cls.__words is None:
            cls.set_words()
            if cls.__words is None:
                print("could not get the words")
        return cls.__words

    # Class method to set the class attribute
    @classmethod
    def set_words(cls):
        i = 0
        with open(os.path.join(wd, '../data/words.txt'), 'r') as file:
            words = file.readlines()
            i += 1
        cls.__words = [zeile.strip() for zeile in words]
