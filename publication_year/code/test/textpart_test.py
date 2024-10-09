import os, sys

os.chdir(os.path.join(os.path.dirname(__file__), '../src'))
sys.path.append(os.getcwd())

from title_module import Title
from textpart import TextPart

import unittest 
  
class TestTextPartModule(unittest.TestCase): 
    part = TextPart("text", Title(28, 39))
    part.text = "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do 2010 eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut 2019 enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum"
    number = part.find_all_titles("consectetur adipiscing elit")

    def test_find_all_titles(self): 
        self.part.titles = sorted(self.part.titles)
        self.assertEqual(self.number, 4)
        for t in self.part.titles:
            title_part = self.part.text[t.start:t.end]
            self.assertTrue(title_part == "consectetur" or title_part == "adipiscing" or title_part == "elit")

    def test_str(self):
        # TextPart:
        #   text: sit amet, consectetur adipiscin...
        #   Titles: 4
        self.assertEqual(self.part.__str__(), "TextPart:\n\ttext: sit amet, consectetur adipiscin...\n\tTitles: 4")

    def test_find_years(self):
        find_years = self.part.find_years()
        self.assertEqual(find_years.year_data[0].__str__(), "2010 (64 - 67) 9")
        self.assertEqual(find_years.year_data[1].__str__(), "2019 (132 - 135) 77")

    def test_calculate_distance(self):
        distance = self.part.calculate_distance(64, 67)
        self.assertEqual(distance, 9)
        distance = self.part.calculate_distance(132, 135)
        self.assertEqual(distance, 77)

if __name__ == '__main__': 
    unittest.main()