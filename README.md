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

* [Hunspell *de_DE_frami* Wörterbuch](https://github.com/LibreOffice/dictionaries/tree/master/de) (.aff & .dic) herunterladen und in ``data/dictionary/`` speichern
* English Spacy Model: ``python3 -m spacy download en_core_web_sm``
* [Clinton & Trump Tweet Dataset](https://www.kaggle.com/benhamner/clinton-trump-tweets) (Kaggle Account notwendig)

---
### Benutzung


##### Beispielaufrufe
