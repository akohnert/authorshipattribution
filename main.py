from feature_extraction.data_set_features import DataSetFeatures
from predict import PredictAuthor
import argparse
import os


def main():
    parser = argparse.ArgumentParser(description='A simple classifier that \
        attributes text to an author.')
    parser.add_argument('mode', help='train from a file or make predictions for \
        a file', choices=('train', 'test'), type=str, action="append")
    parser.add_argument('file', help='file to train or test with (.csv)')
    parser.add_argument('-m', '--model', nargs='?', help='where to save the \
        trained model/which model to use for testing', default='aggregated_\
        features.csv')
    args = parser.parse_args()

    mode = args.mode[0]

    if mode == 'train':
        f = DataSetFeatures(args.file)
        f.extract_features()
        f.aggregate_features(args.model)

    if mode == 'test':
        if os.path.isfile(args.model):
            p = PredictAuthor()
            p.predict(args.file, args.model, 'predictions.csv')
            accuracy = p.evaluate()
            print('\n==== ACCURACY ====')
            for author in accuracy:
                print(author + ': ' + str(accuracy[author]))
        else:
            print("Model file not found. Train model to create one.")


if __name__ == '__main__':
    main()
