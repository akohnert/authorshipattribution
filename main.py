import pandas as pd
from feature_extraction.data_set_features import DataSetFeatures
from predict import PredictAuthor
import argparse
import os


def main():
    parser = argparse.ArgumentParser(description='A simple classifier who attributes text to an author.')
    parser.add_argument('mode', help='either train from a file or make predictions for a file', choices=('train', 'test'), type=str, action="append")
    parser.add_argument('file', help='file to train or test with (.csv)')
    args = parser.parse_args()

    mode = args.mode[0]

    if mode == 'train':
        f = DataSetFeatures(args.file)
        print('Extracting Features ... ')
        f.extract_features()
        f.aggregate_features('aggregated_features.csv')

    if mode == 'test':
        if os.path.isfile('aggregated_features.csv'):
            p = PredictAuthor()
            print('Extracting Features ... ')
            p.best_match(args.file, 'aggregated_features.csv')
            p.save_predictions('predictions.csv')
            p.evaluate()
        else:
            print('aggregated_features.csv is missing. Did you train the model?')


if __name__ == '__main__':
    main()
