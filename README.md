Annalena Kohnert
## **Authorship Attribution**
---
### Installation

Für Linux, Python 3.6


##### 1. Virtual Environment einrichten

````
python3 -m venv venv
. venv/bin/activate
pip install -r requirements.txt
````


##### 2. Benötigte Tools und Daten ggf. herunterladen

* English Spacy Model: ``python3 -m spacy download en_core_web_sm``
* [Clinton & Trump Tweet Dataset](https://www.kaggle.com/benhamner/clinton-trump-tweets) (Kaggle Account notwendig)

---
### Benutzung

1. Zuerst die Daten in Trainings-, Test- und Validierungsdaten splitten:
    ```
    usage: split_data.py DATA_SET [OUTPUT_PATH]
    ```

2. Klassifizierer mit ``main.py`` aufrufen und auf den Daten trainieren und/oder testen:

    ```
    usage: main.py [-h] {train,test} file

    A simple classifier who attributes text to an author.

    positional arguments:
      {train,test}  either train from a file or make predictions for a file
      file          file to train or test with (.csv)

    optional arguments:
      -h, --help    show this help message and exit
    ```


##### Beispielaufrufe

1. ``python3 split_data.py data/hillary_trump_tweets.csv data/``
2. ``python3 main.py train data/train_set.csv``
2. ``python3 main.py test data/test_set.csv``
