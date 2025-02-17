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

    def combine_year_data(self, other):
        for year in other.year_data:
            self.__year_data.add(year)
        return self

    def find_best_year(self):
        if self is None or len(self.__year_data) == 0:
            print("No year data found")
            return None
        for year in self.__year_data:
            year.calculate_score()
        return max(self.__year_data, key=lambda x: x.score)

    def contains(self, year):
        for y in self.year_data:
            if y.year == year:
                return True

    def __str__(self):
        text = ""
        for y in self.year_data:
            text += y.__str__() + "; "
        return text
