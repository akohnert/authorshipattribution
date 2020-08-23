class CharFeatures:

    def __init__(self):
        self.functions = [
                         self.char_sum,
                         str.isalpha,
                         str.isnumeric,
                         str.islower,
                         str.isupper,
                         str.isspace
                         ]

    def feature_occurences(self, text):
        results = []
        for func in self.functions:
            n = 0
            for char in text:
                if func(char):
                    n += 1
            results.append(n)
        return results

    def char_sum(self, text):
        return len(text)
