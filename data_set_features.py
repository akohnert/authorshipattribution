from extract_features import TweetFeatures
import pandas as pd
from collections import Counter

class DataSetFeatures:

    def __init__(self, data_set):
        self.data = pd.read_csv(data_set)
        self.features = self.extract_features()

    def extract_features(self):
        pd.set_option('mode.chained_assignment', None)
        feature_data = pd.DataFrame()
        feature_data['tweet_id'] = [id for id in self.data.id]
        feature_data['author'] = [handle for handle in self.data.handle]
        for i, tweet in self.data.iterrows():
            if i in range(14):
                f = FeatureExtraction(tweet).all_features()
                for key, val in f.items():
                    if key not in feature_data:
                        feature_data[key] = [0.0 for i in self.data.index]
                    feature_data[key][i] = val
        return feature_data

    def save_features(self, filename):
        self.features.to_csv(filename)

    def aggregate_features(self, filename):
        aggregated_features = pd.DataFrame()
        for author in self.features.author.unique():
            agg = Counter()
            subset = self.features[self.features['author'] == author]
            for col in subset:
                if col not in ['tweet_id', 'author']:
                    agg[col] = subset[col].mean()
            keys = ['author'] + [key for (key, val) in agg.items()]
            vals = [author] + [val for (key, val) in agg.items()]
            author_agg = pd.DataFrame([vals], columns=keys)
            if aggregated_features.empty:
                aggregated_features = pd.DataFrame([vals], columns=keys)
            else:
                aggregated_features = aggregated_features.append(author_agg, ignore_index=True)
        aggregated_features.to_csv(filename)
