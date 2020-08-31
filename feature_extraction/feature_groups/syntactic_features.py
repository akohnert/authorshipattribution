from collections import Counter
from feature_extraction.feature_groups.FeatureBaseClass import Features


class SyntacticFeatures(Features):

    def __init__(self):
        self.functions = {
                         'POS': self.pos,
                         }
        self.output = {}

    def feature_occurences(self, preprocessed_text):
        results = {}
        for func in self.functions:
            results = {**results, **self.functions[func](preprocessed_text)}
        return results

    def pos(self, preprocessed_text):
        c = Counter()
        pos = preprocessed_text['pos']
        tokens = preprocessed_text['tokens']
        token_sum = sum(len(sentence) for sentence in tokens)
        for tag in pos:
            c[tag] += 1
        for tag in pos:
            c[tag] = c[tag] / token_sum
        return c
