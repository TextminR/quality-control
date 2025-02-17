from extract import ExtractInterface
from year_data import YearData
from year_list import YearList
from transformers import pipeline

class Ner(ExtractInterface):

    def __init__(self):
        self.classifier = self.load()

    def load(self):
        model_id = 'textminr/ner-multilingual-bert'

        classifier = pipeline(
          'ner',
          model=model_id,
          aggregation_strategy='simple'
        )
        return classifier

    def find_years(self, text):
        n_digites = 0
        year_start, year_end = 0, 0
        year = ""
        year_list = YearList()

        responses = self.classifier(text)

        print(responses)
