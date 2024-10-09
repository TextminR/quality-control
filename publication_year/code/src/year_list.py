from year_data import YearData

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
        text = ""
        for y in self.year_data:
            text += y.__str__() + "; "
        return text

if __name__ == "__main__":
    yl = YearList()
    y1 = YearData(1911, 11, 14, 10, 99.9)
    y2 = YearData(1912, 22, 25, 30, 89.9)
    yl.add_year(y1)
    yl.add_year(y2)
    print(yl)

