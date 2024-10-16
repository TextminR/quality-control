import os, sys

os.chdir(os.path.join(os.path.dirname(__file__), '../src'))
sys.path.append(os.getcwd())

from year_list import YearList
from year_data import YearData

import unittest 
  
class TestTextPartModule(unittest.TestCase): 
    ylist = YearList()
    ylist.add_year(YearData(2010, 64, 67, 9))
    ylist.add_year(YearData(1910, 74, 77, 6))
    ylist.add_year(YearData(1810, 84, 87, 3))
    ylist.add_year(YearData(1850, 94, 97, 12))

    def test_year_list(self): 
        self.ylist.clear_years(1800, 1900)
        self.assertEqual(self.ylist.year_data.pop().__str__(), "Y:1850 (94 - 97) 12")
        self.assertEqual(self.ylist.year_data.pop().__str__(), "Y:1810 (84 - 87) 3")

if __name__ == '__main__': 
    unittest.main()