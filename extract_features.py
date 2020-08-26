from LinguisticPreprocessing import Preprocessing
from features.character_based_features import CharFeatures
from features.punctuation_based_features import PunctFeatures
from features.word_based_features import WordFeatures
from features.syntactic_features import SyntacticFeatures
from features.semantic_features import SemanticFeatures
from features.meta_based_features import MetaFeatures
from features.sentence_based_features import SentenceFeatures


class FeatureExtraction:

    def __init__(self, tweet):
        self.tweet = tweet

        self.feature_groups = [
                              self.text_features,
                              self.meta_features
                              ]
        self.text_features = [
                             CharFeatures,
                             PunctFeatures,
                             WordFeatures,
                             SyntacticFeatures,
                             SemanticFeatures,
                             SentenceFeatures
                             ]

    def linguistic_features(self):
        self.linguistic_features = Preprocessing(self.tweet.text).output
        return self.linguistic_features

    def text_features(self):
        features = {}
        for feature in self.text_features:
            f = feature()
            new_features = f.feature_occurences(self.tweet.text)
            features = {**features, **new_features}
        return features

    def meta_features(self):
        f = MetaFeatures()
        features = f.feature_occurences(self.tweet)
        return features

    def all_features(self, save=True):
        features = {}
        for group in self.feature_groups:
            new_features = group()
            features = {**features, **new_features}
        return features
