from collections import Counter
from feature_extraction.feature_groups.FeatureBaseClass import Features


class PunctFeatures(Features):

    def __init__(self):
        self.symbols = ',;.:!?-'

    def feature_occurences(self, text):
        results = Counter()
        for symbol in self.symbols:
            for char in text:
                if symbol == char:
                    results[symbol] += 1
            results[symbol] = results[symbol] / len(text)
        return results
