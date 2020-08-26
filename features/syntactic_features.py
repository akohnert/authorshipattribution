from LinguisticPreprocessing import Preprocessing
from collections import Counter

class SyntacticFeatures:

    def __init__(self):
        self.functions = {
                         'POS' : self.pos,
                         }
        self.output = {}

    def feature_occurences(self, text):
        results = {}
        for func in self.functions:
            results = {**results, **self.functions[func](text)}
        return results

    def spacy_pipeline(self, text):
        if not self.output:
            self.output = Preprocessing(text).output

    def pos(self, text):
        c = Counter()
        self.spacy_pipeline(text)
        pos = self.output['pos']
        tokens = self.output['tokens']
        token_sum = sum(len(sentence) for sentence in tokens)
        for tag in pos:
            c[tag] += 1
        for tag in pos:
            c[tag] = c[tag] / token_sum
        return c
