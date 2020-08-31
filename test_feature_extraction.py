from feature_extraction.LinguisticPreprocessing import Preprocessing
from feature_extraction.feature_groups.character_based_features import CharFeatures
from feature_extraction.feature_groups.punctuation_based_features import PunctFeatures
from feature_extraction.feature_groups.word_based_features import WordFeatures
from feature_extraction.feature_groups.sentence_based_features import SentenceFeatures
import unittest


'''
Testet ausgewählte (meist selbst berechnete) text-basierten Features (sowohl
mit als auch ohne Preprocessing), aber nicht die Meta Features, die direkt aus
der csv-Datei abgelesen werden.
'''


class FeatureExtractionTest(unittest.TestCase):

    def setUp(self):
        self.test_tweets = [
                           "When you work hard, you should not be living in poverty. https://t.co/86sTOCAkkq",
                           "Trump told 31 outright lies just last week.\n\nKeep him honest at tonight's debate: Follow @TheBriefing2016 to get th… https://t.co/m1WyJ3DJqF",
                           "Such a great honor. Final debate polls are in - and the MOVEMENT wins!\n#AmericaFirst #MAGA #ImWithYou… https://t.co/DV1BKMwHEM",
                           "The new @NMAAHC is an overdue tribute to African American history. Let's build a more open, inclusive future by reflecting on our past. -H"
                           ]

        self.char_features = [{'alpha chars': 60/80, 'lower chars': 55/80,
                               'space chars': 11/80, 'upper chars': 5/80,
                               'numeric chars': 2/80},
                              {'alpha chars': 102/140, 'lower chars': 92/140,
                               'space chars': 20/140, 'upper chars': 10/140,
                               'numeric chars': 8/140},
                              {'alpha chars': 96/126, 'lower chars': 69/126,
                               'space chars': 17/126, 'upper chars': 27/126,
                               'numeric chars': 1/126},
                              {'alpha chars': 109/138, 'lower chars': 98/138,
                               'space chars': 23/138, 'upper chars': 11/138,
                               'numeric chars': 0}
                              ]

        self.punct_features = [{',': 1/80, '.': 2/80, ';': 0, ':': 1/80,
                                '!': 0, '?': 0, '-': 0},
                               {',': 0, '.': 2/140, ';': 0, ':': 2/140,
                                '!': 0, '?': 0, '-': 0},
                               {',': 0, '.': 2/126, ';': 0, ':': 1/126,
                                '!': 1/126, '?': 0, '-': 1/126},
                               {',': 1/138, '.': 2/138, ';': 0, ':': 0,
                                '!': 0, '?': 0, '-': 1/138}
                               ]

        self.word_features = [{'avg. token length': 69/14, 'hashtag': 0,
                               'URL': 1/14, 'mention': 0, 'emoticon': 0,
                               'symbol': 2/14, 'uppercase tokens': 0,
                               'numeric tokens': 0, 'alphabet-only tokens':
                               11/14},
                              {'avg. token length': 120/24, 'hashtag': 0,
                               'URL': 1/24, 'mention': 1/24, 'emoticon': 0,
                               'symbol': 3/24, 'uppercase tokens': 0,
                               'numeric tokens': 1/24, 'alphabet-only tokens':
                               17/24},
                              {'avg. token length': 109/21, 'hashtag': 3/21,
                               'URL': 1/21, 'mention': 0, 'emoticon': 0,
                               'symbol': 4/21, 'uppercase tokens': 2/21,
                               'numeric tokens': 0, 'alphabet-only tokens':
                               13/21},
                              {'avg. token length': 115/29, 'hashtag': 0,
                               'URL': 0, 'mention': 1/29, 'emoticon': 0,
                               'symbol': 4/29, 'uppercase tokens': 2/29,
                               'numeric tokens': 0, 'alphabet-only tokens':
                               23/29},
                              ]

        self.sentence_features = [{'number sentences': 1, 'chars per sentence':
                                   69, 'tokens per sentence': 14},
                                  {'number sentences': 2, 'chars per sentence':
                                   120/2, 'tokens per sentence': 24/2},
                                  {'number sentences': 2, 'chars per sentence':
                                   109/2, 'tokens per sentence': 21/2},
                                  {'number sentences': 2, 'chars per sentence':
                                   115/2, 'tokens per sentence': 29/2}
                                  ]

    def test_char_features(self):
        for i, tweet in enumerate(self.test_tweets):
            calculated_features = CharFeatures().feature_occurences(tweet)
            for feature in calculated_features:
                self.assertAlmostEqual(calculated_features[feature],
                                       self.char_features[i][feature])

    def test_punct_features(self):
        for i, tweet in enumerate(self.test_tweets):
            calculated_features = PunctFeatures().feature_occurences(tweet)
            for feature in calculated_features:
                self.assertAlmostEqual(calculated_features[feature],
                                       self.punct_features[i][feature])

    def test_sentence_features(self):
        for i, tweet in enumerate(self.test_tweets):
            tweet = Preprocessing(tweet).output
            calculated_features = SentenceFeatures().feature_occurences(tweet)
            for feature in calculated_features:
                self.assertAlmostEqual(calculated_features[feature],
                                       self.sentence_features[i][feature])

    def test_word_features(self):
        for i, tweet in enumerate(self.test_tweets):
            tweet = Preprocessing(tweet).output
            calculated_features = WordFeatures().feature_occurences(tweet)
            for feature in calculated_features:
                self.assertAlmostEqual(calculated_features[feature],
                                       self.word_features[i][feature])


if __name__ == '__main__':
    unittest.main()
