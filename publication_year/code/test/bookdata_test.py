import os, sys

os.chdir(os.path.join(os.path.dirname(__file__), '../src'))
sys.path.append(os.getcwd())

from bookdata import Bookdata

import unittest 
  
class TestBookdataModule(unittest.TestCase): 
    book = Bookdata("Keller, Helen", "di.e: ,Das Ge,schichte: meines lebens", 1880, 1880, 1968)

    def test_set(self):
        self.assertEqual(self.book.author, "Keller, Helen")
        self.assertEqual(self.book.title, "di.e: ,Das Ge,schichte: meines lebens")
        self.assertEqual(self.book.title_clean, "Geschichte meines lebens")
        self.assertEqual(self.book.old_date, 1880)
        self.assertEqual(self.book.birth, 1880)
        self.assertEqual(self.book.death, 1968)
        pass

    def test_string(self): 
        self.assertEqual(self.book.__str__(), "Keller, Helen [1880-1968]: \"di.e: ,Das Ge,schichte: meines lebens\" (1880)")

if __name__ == '__main__': 
    unittest.main()
