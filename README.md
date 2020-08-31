**PRO-2A SoSe 2020 Modulprojekt** \
Annalena Kohnert \
Matrikelnr. 785523 \
ankohnert@uni-potsdam.de

---
## **Authorship Attribution**


### Funktion

Das Programm ordnet einem Text einen Autor aus einer Auswahl von zwei oder mehr Autoren zu.

Im **Trainings-Mode** werden die Features aller Tweets in den Trainingsdaten extrahiert und für jeden Autor der Mittelwert jedes Features gebildet. Diese Mittelwerte werden als Modell gespeichert, ebenso werden die extrahierten Features gespeichert (beide als csv-Datei).

Im **Test-Mode** werden die Features für alle Tweets in den Testdaten extrahiert und dann für jeden Tweet die Distanz zum Mittelwert für jeden Autor (wie beim Training errechnet) bestimmt. Der Autor mit der niedrigsten Distanz wird als Vorhersage ausgewählt, die extrahierten Features mit tatsächlichem and vorhergesagtem Autor gespeichert und es wird die Präzision (*Accuracy*) der Klassifikation sowohl für die einzelnen Autoren als auch für alle Tweets ausgegeben.

### Daten

Der Klassifizier liest Trainungs- und Testdaten aus csv-Dateien ein und speichert alle Ausgaben auch in diesem Format. \
Grundlegend notwendig sind die Reihen/Attribute ``handle`` (Twitter-Usernamen oder irgendeinen String als Name des Autors), ``text`` (der Text bzw. Tweet als String) und ``id`` (die Tweet ID bzw. irgendeine Art eindeutige Identifizierung). \
Für die Meta Features werden außerdem ``is_retweet``, ``is_quote_status`` und ``truncated`` (Boolsche Werte) und ``original_author`` und ``in_reply_to_screen_name`` (Strings) erwartet. Weitere Features basierend auf anderen Attributen können noch hinzugefügt werden oder wieder entfernt werden.

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

### Benutzung

1. Zuerst die Daten in Trainings-, Test- und Validierungsdaten splitten:
    ```
    usage: split_data.py DATA_SET [OUTPUT_PATH]
    ```
    Erzeugt beim Standardaufruf die drei Dateien ``'train.csv'``, ``'test.csv'`` und ``'dev.csv'``.

2. Klassifizierer mit ``main.py`` aufrufen und auf den Daten trainieren und/oder testen:

    ```
    usage: main.py [-h] [--model [MODEL]] [--train_features [TRAIN_FEATURES]]
                   [--output [OUTPUT]]
                   {train,test} file

    A simple classifier that attributes text to an author.

    positional arguments:
      {train,test}          train from a file or make predictions for a file
      file                  file to train or test with (.csv)

    optional arguments:
      -h, --help            show this help message and exit
      --model [MODEL]       where to save the trained model/which model to use for
                            testing (default is model.csv)
      --train_features [TRAIN_FEATURES]
                            where to save the features used for training (default
                            is train_features.csv)
      --output [OUTPUT]     where to save the predictions (default is
                            predictions.csv)
    ```

3. Unittest aufrufen:
    ```
    python3 test_feature_extraction.py
    ```

##### Beispielaufrufe

1. ``python3 split_data.py data/hillary_trump_tweets.csv data/``
2. ``python3 main.py train data/train.csv``
2. ``python3 main.py test data/test.csv``
