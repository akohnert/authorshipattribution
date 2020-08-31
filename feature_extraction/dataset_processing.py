from feature_extraction.tweet_features import TweetFeatures
import pandas as pd
from collections import Counter
import tqdm
import logging

logging.basicConfig(filename=".log", level=logging.DEBUG, format=
                    "%(asctime)s:%(pathname)s:%(levelname)s:%(message)s")


class DataSetProcessing:

    def __init__(self, filename):
        self.filename = filename
        self.data = pd.read_csv(filename)
        self.features = pd.DataFrame()

    def extract_features(self):
        # SettingWithCopyWarning ausschalten, überschreiben ist gewollt
        pd.set_option('mode.chained_assignment', None)
        self.features['tweet_id'] = [id for id in self.data.id]
        self.features['author'] = [handle for handle in self.data.handle]
        # auf stdout Fortschritt/verbleibende Zeit anzeigen
        print('Extracting features from {} ...'.format(self.filename))
        with tqdm.tqdm(total=self.data.shape[0]) as pbar:
            for i, tweet in self.data.iterrows():
                # jeden verarbeiteten Tweet loggen
                logging.info('Processing tweet with ID {}'
                             .format(self.features['tweet_id'][i]))
                f = TweetFeatures(tweet).extract_features()
                # jedes Features hinzufügen,
                # leere bzw. nicht-vorhandene Features ggf. mit 0 auffüllen
                for key, val in f.items():
                    if key not in self.features:
                        self.features[key] = [0.0 for i in self.data.index]
                    self.features[key][i] = val
                pbar.update(1)
        return self.features

    def save_features(self, filename):
        logging.info('Saving extracted features to {}'.format(filename))
        self.features.to_csv(filename)

    def aggregate_features(self, filename):
        aggregated_features = pd.DataFrame()
        # für jeden Autor Mittelwert aller Feature bilden
        for author in self.features.author.unique():
            agg = Counter()
            subset = self.features[self.features['author'] == author]
            for col in subset:
                # Nicht-Feature Informationen ausschließen
                if col not in ['tweet_id', 'author']:
                    agg[col] = subset[col].mean()
            # keys: Feature-Name
            # val: Feature-(Mittel)wert
            keys = ['author'] + [key for (key, val) in agg.items()]
            vals = [author] + [val for (key, val) in agg.items()]
            # Feature-Mittelwerte zu DataFrame hinzufügen
            author_agg = pd.DataFrame([vals], columns=keys)
            if aggregated_features.empty:
                aggregated_features = pd.DataFrame([vals], columns=keys)
            else:
                aggregated_features = aggregated_features.append(author_agg)
        logging.info('Saving aggregated features to {}'.format(filename))
        aggregated_features.to_csv(filename)
