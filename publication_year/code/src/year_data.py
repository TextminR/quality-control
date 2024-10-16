
class YearData:
    def __init__(self, year, start, end, distance, score=None):
        self.__year = year
        self.__start = start
        self.__end = end
        self.__distance = distance
        self.__score = score
    
    @property
    def year(self):
        return self.__year
    
    @year.setter
    def year(self, value):
        self.__year = value

    @property
    def start(self):
        return self.__start
    
    @start.setter
    def start(self, value):
        self.__start = value

    @property
    def end(self):
        return self.__end
    
    @end.setter
    def end(self, value):
        self.__end = value

    @property
    def distance(self):
        return self.__distance
    
    @distance.setter
    def distance(self, value):
        self.__distance = value
    
    @property
    def score(self):
        return self.__score
        
    @score.setter
    def score(self, value):
        self.__score = value

    def __hash__(self):
        return hash((self.year, self.start, self.end, self.distance, self.score))

    # Year: 2029 (11 - 14), Distance: 15, Score: 0.0
    # 2011 (11 - 14) 15: 99.9
    def __str__(self):
        text = f"Y:{self.year} ({self.start} - {self.end}) {self.distance}"
        if self.score is not None:
            text += f" | {self.score}"
        return text