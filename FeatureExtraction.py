from LinguisticProcessing import LinguisticProcessing
import pandas as pd


class FeatureExtration:

    def __init__(self, input):
        self.data = pd.read_csv(input, encoding='utf-8')
        self.l = LinguisticProcessing()

    def linguistic_preprocessing(self):
        for text in self.data.text:
            sentences, types = self.l.tokenizer(text)
            self.l.spacy(sentences)
            #self.l.spacy(text)

if __name__ == '__main__':
    fe = FeatureExtration('hillary_trump_tweets.csv')
    fe.linguistic_preprocessing()
