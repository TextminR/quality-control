from extract import ExtractInterface
from year_data import YearData
from year_list import YearList
import re

class Manual(ExtractInterface):

    def find_years(self, text):
        n_digites = 0
        year_start, year_end = 0, 0
        year = ""
        year_list = YearList()
        for i in range(0, len(text)):
            c = text[i]
            if bool(re.fullmatch(r"[0-9]+", c)):

                if n_digites > 4:
                    n_digites = 0
                    year = ""
                    continue
                if n_digites == 0:
                    year_start = i
                n_digites += 1
                year += c
            else:
                if n_digites > 0 and n_digites <= 4:
                    year_end = i - 1
                    try:
                        year = int(year)

                        year_data = YearData(year, year_start, year_end)
                        year_list.add_year(year_data)
                    except:
                        raise TypeError("could not parse, year is not a number")
                n_digites = 0
                year = ""
        return year_list
