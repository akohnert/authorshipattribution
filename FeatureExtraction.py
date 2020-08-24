from LinguisticPreprocessing import Preprocessing
import pandas as pd
from collections import Counter
from textblob import TextBlob


class FeatureExtraction:

    def __init__(self):
        self.ling = Preprocessing()


    def sentiment(self, text):
        analysis = TextBlob(text)
        if analysis.sentiment.polarity > 0:
            return 'positive'
        elif analysis.sentiment.polarity == 0:
            return 'neutral'
        else:
            return 'negative'
