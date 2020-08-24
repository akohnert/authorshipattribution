from LinguisticPreprocessing import Preprocessing
from FeatureExtraction import FeatureExtraction
from features.character_based_features import CharFeatures
from features.punctuation_based_features import PunctFeatures
from features.word_based_features import WordFeatures
from features.syntactic_features import SyntacticFeatures
from features.semantic_features import SemanticFeatures

import pandas as pd

def main():
    data = pd.read_csv('../dev_set.csv')
    f = FeatureExtraction()
    l = Preprocessing()
    cf = CharFeatures()
    pf = PunctFeatures()
    wf = WordFeatures()
    sf = SyntacticFeatures()
    semf = SemanticFeatures()
    for text in data.text:
        pass


if __name__ == '__main__':
    main()
