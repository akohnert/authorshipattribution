from LinguisticPreprocessing import Preprocessing
from collections import Counter

class SyntacticFeatures:

    def __init__(self):
        self.ling = Preprocessing()

    def pos_frequencies(self, text):
        c = Counter()
        pos, lemma = self.ling.pos_lemma(text)
        token_sum = sum(len(sentence) for sentence in self.ling.tokenizer(text)[0])
        for tag in pos:
            c[tag] += 1
        for tag in pos:
            c[tag] = c[tag] / token_sum
        return c
