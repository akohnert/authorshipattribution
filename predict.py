from feature_extraction.dataset_processing import DataSetProcessing
import pandas as pd
from collections import Counter
import logging

logging.basicConfig(filename=".log", level=logging.DEBUG, format=
                    "%(asctime)s:%(pathname)s:%(levelname)s:%(message)s")


class PredictAuthor:

    def __init__(self):
        self.data = pd.DataFrame()
        self.model = pd.DataFrame()
        self.predictions = []

    # Besten bzw. wahrscheinlichsten Autor für jeden Tweet bestimmen
    def best_match(self, test_file, model):
        model = pd.read_csv(model)
        self.data = DataSetProcessing(test_file).extract_features()
        # für jeden Tweet Distanz jedes Features zum Modell errechnen
        for i in self.data.index:
            D = Counter()
            for feature in self.data:
                if feature not in ['author', 'tweet_id']:
                    for j in model.index:
                        # Wenn Testdaten Features enthalten, die nicht im
                        # Modell sind, werden sie ignoriert
                        if feature not in model:
                            logging.warning('Feature "{}" not in model.'.
                            format(feature)+' Feature is ignored.')
                        else:
                            d = self.data[feature][i]-model[feature][j]
                            D[model['author'][j]] += abs(d)
            self.predictions.append(min(D, key=D.get))
        assert(len(self.predictions) == self.data.shape[0])

    # Vorhersagen für Tesdaten machen und speichern
    def predict(self, test_file, model, filename=""):
        self.best_match(test_file, model)
        self.data.insert(loc=2, column='predicted_author',
                         value=self.predictions)
        if filename:
            logging.info('Saving predictions to {}'.format(filename))
            self.data.to_csv(filename)
        return self.data, self.predictions

    # Accuracy für jeden einzelnen Autor als auch insgesamt errechnen
    def evaluate(self):
        if self.data.empty:
            raise Exception()
        matches = Counter()
        for author in self.data.author.unique():
            tweets = self.data.index[self.data.author == author].tolist()
            for i in tweets:
                if self.data.author[i] == self.data.predicted_author[i]:
                    matches[author] += 1
                    matches['Overall Accuracy'] += 1
            matches[author] = matches[author] / len(tweets)
        matches['Overall Accuracy'] /= self.data.shape[0]
        return matches
