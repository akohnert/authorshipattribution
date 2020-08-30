from feature_extraction.tweet_features import TweetFeatures
import pandas as pd
from collections import Counter
import tqdm


class DataSetFeatures:

    def __init__(self, filename):
        self.filename = filename
        self.data = pd.read_csv(filename)
        self.features = pd.DataFrame()

    def extract_features(self):
        pd.set_option('mode.chained_assignment', None)
        self.features['tweet_id'] = [id for id in self.data.id]
        self.features['author'] = [handle for handle in self.data.handle]
        print('Extracting features from ' + self.filename + ' ...')
        with tqdm.tqdm(total=self.data.shape[0]) as pbar:
            for i, tweet in self.data.iterrows():
                f = TweetFeatures(tweet).extract_features()
                for key, val in f.items():
                    if key not in self.features:
                        self.features[key] = [0.0 for i in self.data.index]
                    self.features[key][i] = val
                pbar.update(1)
        return self.features

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
                aggregated_features = aggregated_features.append(author_agg)
        aggregated_features.to_csv(filename)
