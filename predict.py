from feature_extraction.tweet_features import TweetFeatures
from feature_extraction.data_set_features import DataSetFeatures
import pandas as pd
from collections import Counter

class PredictAuthor:

    def __init__(self):
        self.test_cases = pd.DataFrame()
        self.predictions = []

    def best_match(self, test_file, train_file):
        predictions = []
        train = pd.read_csv(train_file)
        test_cases = DataSetFeatures(test_file).extract_features()
        for i in test_cases.index:
            D = Counter()
            for feature in test_cases:
                if feature not in ['author', 'tweet_id']:
                    for j in train.index:
                        D[train['author'][j]] += abs(test_cases[feature][i]-train[feature][j])
            predictions.append(min(D, key=D.get))
        assert(len(predictions) == test_cases.shape[0])
        self.test_cases = test_cases
        self.predictions  = predictions
        return test_cases, predictions

    def save_predictions(self, filename):
        if self.test_cases.empty:
            raise Exception()
        self.test_cases.insert(loc=2, column='predicted_author', value=self.predictions)
        self.test_cases.to_csv(filename)

    def evaluate(self):
        if self.test_cases.empty:
            raise Exception()
        matches = Counter()
        for author in self.test_cases.author.unique():
            tweets_by_author = self.test_cases.index[self.test_cases.author == author].tolist()
            for i in tweets_by_author:
                if self.test_cases.author[i] == self.test_cases.predicted_author[i]:
                    matches[author] += 1
                    matches['total'] += 1
            matches[author] = matches[author] / len(tweets_by_author)
        matches['total'] = matches['total'] / self.test_cases.shape[0]
        # nur vorerst
        print(matches)
        return matches
