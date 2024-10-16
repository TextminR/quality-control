from year_data import YearData

class YearList:
    def __init__(self):
        self.year_data = set()

    @property
    def year_data(self):
        return self.__year_data
    
    @year_data.setter
    def year_data(self, value):
        self.__year_data = value

    def add_year(self, year):
        self.__year_data.add(year)

    def clear_years(self, birth, death):
        new_year_data = set()
        for year in self.__year_data:
            y = year.year
            if y >= birth and y <= death:
                new_year_data.add(year)
        self.__year_data = new_year_data
        return self

    def __str__(self):
        text = ""
        for y in self.year_data:
            text += y.__str__() + "; "
        return text
