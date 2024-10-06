
class Title:
    def __init__(self, start, end):
        self.__start = start
        self.__end = end

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
    
    def __str__(self):
        return f"({self.start} - {self.end})"
    
    def __hash__(self) -> int:
        return hash((self.start, self.end))
    
    def __eq__(self, other) -> bool:
        return self.start == other.start and self.end == other.end