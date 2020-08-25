from LinguisticPreprocessing import Preprocessing
from collections import Counter

class SyntacticFeatures:

    def __init__(self):
        self.output = {}

    def feature_occurences(self, text):
        if not self.output:
            self.output = Preprocessing(text).output
        c = Counter()
        pos = self.output['pos']
        token_sum = sum(len(sentence) for sentence in Preprocessing().tokenizer(text)[0])
        for tag in pos:
            c[tag] += 1
        for tag in pos:
            c[tag] = c[tag] / token_sum
        return c
