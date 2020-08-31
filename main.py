from feature_extraction.dataset_processing import DataSetProcessing
from predict import PredictAuthor
import argparse
import os


"""
Für Benutzeraufrufe: Benutzer kann Argumente übergeben und traineren oder
testen und sich die Benutzung des Programms erklären  lassen.
"""


def main():
    parser = argparse.ArgumentParser(description='A simple classifier that \
                                     attributes text to an author.')
    parser.add_argument('mode', help='train from a file or make predictions for \
                        a file', choices=('train', 'test'), type=str,
                        action="append")
    parser.add_argument('file', help='file to train or test with (.csv)')
    parser.add_argument('--model', nargs='?', help='where to save the \
                        trained model/which model used for testing (default \
                        is model.csv)', default='model.csv')
    parser.add_argument('--train_features', nargs='?', help='where to save the \
                        features used for training (default is \
                        train_features.csv)', default='train_features.csv')
    parser.add_argument('--output', nargs='?', help='where to save the \
                        predictions (default is predictions.csv)',
                        default='predictions.csv')
    args = parser.parse_args()

    mode = args.mode[0]

    if mode == 'train':
        f = DataSetProcessing(args.file)
        f.extract_features()
        f.save_features(args.train_features)
        f.aggregate_features(args.model)

    if mode == 'test':
        if os.path.isfile(args.model):
            p = PredictAuthor()
            p.predict(args.file, args.model, args.output)
            accuracy = p.evaluate()
            print('\n==== ACCURACY ====')
            for author in accuracy:
                print(author + ': ' + str(accuracy[author]))
        else:
            print("Model file not found. Train model to create one.")


if __name__ == '__main__':
    main()
