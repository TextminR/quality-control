
class YearData:
    def __init__(self, year, start, end, distance = None, line_distance = None, score=None):
        self.__year = year
        self.__start = start
        self.__end = end
        self.__distance = distance
        self.__line_distance = line_distance 
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
    def line_distance(self):
        return self.__line_distance
    
    @line_distance.setter
    def line_distance(self, value):
        self.__line_distance = value

    @property
    def score(self):
        return self.__score
        
    @score.setter
    def score(self, value):
        self.__score = value

    def calculate_score(self):
        if self.distance is None or self.line_distance is None:
            self.score = 0
            return
        # size of the text part
        margin = 150
        # higher the distance, lower the score
        score_distance = 1 - self.distance/(2*margin)
        # higher the line distance, lower the score
        score_line_distance =  1 - self.line_distance/2

        self.score = (score_distance + score_line_distance) / 2

    def __hash__(self):
        return hash((self.year, self.start, self.end, self.distance, self.line_distance, self.score))

    # Year: 2029 (11 - 14), Distance: 15, Score: 0.0
    # 2011 (11 - 14) 15: 99.9
    def __str__(self):
        text = f"Y:{self.year} ({self.start} - {self.end}) {self.distance}: {self.__line_distance}"
        if self.score is not None:
            text += " | {" + str(round(self.score, 2)) + "}"
        return text
