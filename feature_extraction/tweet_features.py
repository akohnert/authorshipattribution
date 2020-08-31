from feature_extraction.linguistic_preprocessing import Preprocessing
from feature_extraction.feature_groups.character_based_features \
    import CharFeatures
from feature_extraction.feature_groups.punctuation_based_features \
    import PunctFeatures
from feature_extraction.feature_groups.word_based_features \
    import WordFeatures
from feature_extraction.feature_groups.syntactic_features \
    import SyntacticFeatures
from feature_extraction.feature_groups.semantic_features \
    import SemanticFeatures
from feature_extraction.feature_groups.meta_features \
    import MetaFeatures
from feature_extraction.feature_groups.sentence_based_features \
    import SentenceFeatures
import logging

'''
Führt die verschiedenen Feature Klassen und Methoden zusammen, führt sie
nacheinander aus und warnt, wenn Namen doppelt vergeben wurden.
'''

logging.basicConfig(filename=".log", level=logging.DEBUG, format=
                    "%(asctime)s:%(pathname)s:%(levelname)s:%(message)s")


class TweetFeatures:

    def __init__(self, tweet):
        self.tweet = tweet

        # Features in Gruppen sortieren
        self.feature_groups = [
                              self.__raw_text_features,
                              self.__preprocessed_text_features,
                              self.__meta_features
                              ]
        self.raw_text_features = [
                                 CharFeatures,
                                 PunctFeatures,
                                 SemanticFeatures
                                 ]
        self.preprocessed_text_features = [
                                          WordFeatures,
                                          SyntacticFeatures,
                                          SentenceFeatures
                                          ]

    # Objekt zu Funktion bei Aufruf
    def __call__(self):
        return self.extract_features()

    def __preprocessed_text_features(self):
        preprocessor = Preprocessing(self.tweet.text)
        tokens = preprocessor()
        features = {}
        for feature in self.preprocessed_text_features:
            f = feature()
            new_features = f.feature_occurences(tokens)
            self.__overwrite_warning(features, new_features)
            features = {**features, **new_features}
        return features

    def __raw_text_features(self):
        features = {}
        for feature in self.raw_text_features:
            f = feature()
            new_features = f.feature_occurences(self.tweet.text)
            self.__overwrite_warning(features, new_features)
            features = {**features, **new_features}
        return features

    def __meta_features(self):
        f = MetaFeatures()
        features = f.feature_occurences(self.tweet)
        return features

    def extract_features(self):
        features = {}
        for group in self.feature_groups:
            new_features = group()
            self.__overwrite_warning(features, new_features)
            features = {**features, **new_features}
        return features

    # Prüfen, ob ein Feature Name mehrmals vergeben wurde
    def __overwrite_warning(self, features, new_features):
        overlap = new_features.keys() & features.keys()
        if overlap:
            logging.debug('Following features are defined more than once: ' +
                          str([i for i in overlap]))
            logging.warning('Overwriting non-unique features')
