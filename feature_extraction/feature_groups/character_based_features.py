from collections import Counter


class CharFeatures:

    def __init__(self):
        self.functions = {
                         'alpha chars': str.isalpha,
                         'numeric chars': str.isnumeric,
                         'lower chars': str.islower,
                         'upper chars': str.isupper,
                         'space chars': str.isspace
                         }

    def feature_occurences(self, text):
        results = Counter()
        for func in self.functions:
            for char in text:
                if self.functions[func](str(char)):
                    results[func] += 1
            results[func] = results[func] / len(text)
        return results
