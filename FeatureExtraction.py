from LinguisticProcessing import LinguisticPreprocessing
import pandas as pd
from collections import Counter


class FeatureExtration:

    def __init__(self, input):
        self.data = pd.read_csv(input, encoding='utf-8')
        self.ling = LinguisticPreprocessing()

    def pos_frequency(self):
        for text in self.data.text:
            c = Counter()
            pos, lemma = self.ling.pos_lemma(text)
            for tag in pos:
                c[tag] += 1
            for tag in pos:
                c[tag] = c[tag] / len(pos)
            print(c)


if __name__ == '__main__':
    f = FeatureExtration('../dev_set.csv')
    f.pos_frequency()
