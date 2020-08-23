class PunctFeatures:

    def __init__(self):
        self.symbols = ',;.:!?-—'

    def feature_occurences(self, text):
        results = []
        for symbol in self.symbols:
            n = 0
            for char in text:
                if symbol == char:
                    n += 1
            results.append(n)
        return results
