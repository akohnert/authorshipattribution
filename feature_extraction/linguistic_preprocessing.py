from somajo import SoMaJo
import spacy
from spacy.tokens import Doc
from spacy.pipeline import SentenceSegmenter
import logging


logging.basicConfig(filename=".log", level=logging.DEBUG, format=
                    "%(asctime)s:%(pathname)s:%(levelname)s:%(message)s")


class Preprocessing:

    def __init__(self, text=""):
        self.output = {
                      'tokens': [],
                      'types': [],
                      'lemma': [],
                      'pos': []
                      }
        # Pipeline definieren
        self.nlp = spacy.load("en_core_web_sm")
        self.nlp.tokenizer = self.custom_tokenizer
        seg = SentenceSegmenter(self.nlp.vocab, strategy=self.custom_segmenter)
        self.nlp.add_pipe(seg, first=True)
        # Optional bei bei Klassenaufruf sofort Object erzeugen/füllen
        if text != "":
            if isinstance(text, str):
                self.output = self.pipeline(text)
            else:
                logging.error("Expected a <class 'str'> object, but got {}. "
                              .format(type(text))+'Exiting program.')
                raise Exception("Expected a <class 'str'> object, but got {}."
                                .format(type(text)))

    # SoMaJo-Tokenisierer aufrufen
    # Zusätzlich zu Token werden Token-Klassen bestimmt
    def tokenizer(self, text):
        tokenizer = SoMaJo("en_PTB")
        tokenized_object = tokenizer.tokenize_text([text])
        sentences = []
        types = []
        for sent in tokenized_object:
            sentence = []
            for token in sent:
                sentence.append(token.text)
                types.append(token.token_class)
            sentences.append(sentence)
        self.output['tokens'] = sentences
        self.output['types'] = types
        return sentences, types

    # Spacys Satzsegmentierer überschreiben, stattdessen die Segmentierung
    # von SoMaJo übernehmen
    def custom_segmenter(self, doc):
        start = 0
        sentence_break = False
        for token in doc:
            if sentence_break:
                yield doc[start:token.i-1]
                start = token.i
                sentence_break = False
            elif token.text == '\n':
                sentence_break = True
        if start < len(doc):
            yield doc[start:len(doc)]

    # Spacy-Tokenisierer mit SoMaJo-Tokenisierer überschreiben
    def custom_tokenizer(self, text):
        seg_text = []
        for sentence in self.tokenizer(text)[0]:
            for token in sentence:
                seg_text.append(token)
            seg_text.append('\n')
        if seg_text[-1] == '\n':
            seg_text.pop(-1)
        return Doc(self.nlp.vocab, seg_text)

    # Gesamte Pipeline aufrufen, ohne Parser/NER
    def pipeline(self, text):
        doc = self.nlp(text, disable=['parser', 'ner'])
        for sent in doc.sents:
            for token in sent:
                self.output['lemma'].append(token.lemma_)
                self.output['pos'].append(token.pos_)
        return self.output
