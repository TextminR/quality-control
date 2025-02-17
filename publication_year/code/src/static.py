import os

wd = os.path.dirname(__file__)
class Static:
    __words = None
    __index = None

    # Class method to get the class attribute words
    @classmethod
    def get_words(cls):
        if cls.__words is None:
            cls.set_words()
            if cls.__words is None:
                print("could not get the words")
        return cls.__words

    # Class method to set the class attribute words
    @classmethod
    def set_words(cls):
        i = 0
        with open(os.path.join(wd, '../data/words.txt'), 'r') as file:
            words = file.readlines()
            i += 1
        cls.__words = [zeile.strip() for zeile in words]

    # Class method to get the class attribute index
    @classmethod
    def get_index(cls):
        if cls.__index is None:
            cls.set_index()
            if cls.__index is None:
                print("could not get the index")
        return cls.__index

    # Class method to set the class attribute index
    @classmethod
    def set_index(cls):
        i = 0
        with open(os.path.join(wd, '../data/index.txt'), 'r') as file:
            index = file.readlines()
            i += 1
        cls.__index = [zeile.strip() for zeile in index]
