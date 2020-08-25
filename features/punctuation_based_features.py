from collections import Counter

class PunctFeatures:

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
