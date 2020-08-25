from textblob import TextBlob

class SemanticFeatures:

    def __init__(self):
        self.functions = {
                         'sentiment' : self.sentiment
                         }

    def feature_occurences(self, text):
        results = {}
        for func in self.functions:
            results[func] = self.functions[func](text)
        return results

    def sentiment(self, text):
        analysis = TextBlob(text)
        if analysis.sentiment.polarity > 0:
            return 1
        elif analysis.sentiment.polarity == 0:
            return 0.5
        else:
            return 0
