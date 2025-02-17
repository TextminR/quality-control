from abc import ABC, abstractmethod
from year_list import YearList

# creating interface
class ExtractInterface(ABC):
    @abstractmethod
    def find_years(self, text):
        return YearList()
