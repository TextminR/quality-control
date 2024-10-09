import os, sys

os.chdir(os.path.join(os.path.dirname(__file__), '../src'))
sys.path.append(os.getcwd())

from title_module import Title

import unittest 
  
class TestTitleModule(unittest.TestCase): 

    def test_init(self): 
        title = Title(1, 5)
        self.assertEqual(title.start, 1) 
        self.assertEqual(title.end, 5)

    def test_str(self):
        title = Title(1, 5)
        self.assertEqual(str(title), "(1 - 5)")
        title = Title(8, 9)
        self.assertEqual(str(title), "(8 - 9)")


if __name__ == '__main__': 
    unittest.main()