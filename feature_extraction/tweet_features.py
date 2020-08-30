from feature_extraction.LinguisticPreprocessing import Preprocessing
from feature_extraction.feature_groups.character_based_features import CharFeatures
from feature_extraction.feature_groups.punctuation_based_features import PunctFeatures
from feature_extraction.feature_groups.word_based_features import WordFeatures
from feature_extraction.feature_groups.syntactic_features import SyntacticFeatures
from feature_extraction.feature_groups.semantic_features import SemanticFeatures
from feature_extraction.feature_groups.meta_based_features import MetaFeatures
from feature_extraction.feature_groups.sentence_based_features import SentenceFeatures


class TweetFeatures:

    def __init__(self, tweet):
        self.tweet = tweet

        self.feature_groups = [
                              self.raw_text_features,
                              self.preprocessed_text_features,
                              self.meta_features
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

    def preprocessed_text_features(self):
        tokens = Preprocessing(self.tweet.text).output
        features = {}
        for feature in self.preprocessed_text_features:
            f = feature()
            new_features = f.feature_occurences(tokens)
            features = {**features, **new_features}
        return features

    def raw_text_features(self):
        features = {}
        for feature in self.raw_text_features:
            f = feature()
            new_features = f.feature_occurences(self.tweet.text)
            features = {**features, **new_features}
        return features

    def meta_features(self):
        f = MetaFeatures()
        features = f.feature_occurences(self.tweet)
        return features

    def extract_features(self):
        features = {}
        for group in self.feature_groups:
            new_features = group()
            features = {**features, **new_features}
        return features
