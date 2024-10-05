import os

wd = os.path.dirname(__file__)
class Static:
    # unwichtige woerter die aus dem titel geloescht werden koenen
    words = None
    def get_words():
        if Static.words is None:
            i = 0
            with open(os.path.join(wd, 'words.txt'), 'r') as file:
                words = file.readlines()
                i += 1

            Static.words = [zeile.strip() for zeile in words]
        return Static.words

Static.get_words()
