
class YearList:
    def __init__(self):
        self.year_data = []

    @property
    def year_data(self):
        return self.__year_data
    
    @year_data.setter
    def year_data(self, value):
        self.__year_data = value

    def add_year(self, year):
        self.__year_data.append(year)

    def __str__(self):
        return f"{self.year_data}"