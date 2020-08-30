from feature_extraction.data_set_features import DataSetFeatures
import pandas as pd
from collections import Counter


class PredictAuthor:

    def __init__(self):
        self.data = pd.DataFrame()
        self.model = pd.DataFrame()
        self.predictions = []

    def best_match(self, test_file, model):
        model = pd.read_csv(model)
        self.data = DataSetFeatures(test_file).extract_features()
        for i in self.data.index:
            D = Counter()
            for feature in self.data:
                if feature not in ['author', 'tweet_id']:
                    for j in model.index:
                        if feature not in model:
                            pass
                        else:
                            d = self.data[feature][i]-model[feature][j]
                            D[model['author'][j]] += abs(d)
            self.predictions.append(min(D, key=D.get))
        assert(len(self.predictions) == self.data.shape[0])

    def predict(self, test_file, model, filename=""):
        self.best_match(test_file, model)
        self.data.insert(loc=2, column='predicted_author',
                         value=self.predictions)
        if filename:
            self.data.to_csv(filename)
        return self.data, self.predictions

    def evaluate(self):
        if self.data.empty:
            raise Exception()
        matches = Counter()
        for author in self.data.author.unique():
            tweets = self.data.index[self.datas.author == author].tolist()
            for i in tweets:
                if self.data.author[i] == self.data.predicted_author[i]:
                    matches[author] += 1
                    matches['Overall Accuracy'] += 1
            matches[author] = matches[author] / len(tweets)
        matches['Overall Accuracy'] /= self.data.shape[0]
        return matches
