from somajo import SoMaJo
import spacy
from spacy.tokens import Doc
from spacy.pipeline import SentenceSegmenter

class Preprocessing:

    def __init__(self):
        self.nlp = spacy.load("en_core_web_sm")
        self.nlp.tokenizer = self.custom_tokenizer
        seg = SentenceSegmenter(self.nlp.vocab, strategy=self.custom_segmenter)
        self.nlp.add_pipe(seg, first=True)

    def tokenizer(self, text):
        tokenizer = SoMaJo("en_PTB")
        tokenized_object = tokenizer.tokenize_text([text])
        sentences = []
        types = []
        for sent in tokenized_object:
            s = []
            t = []
            for token in sent:
                s.append(token.text)
                t.append(token.token_class)
            sentences.append(s)
            types.append(t)
        return sentences, types

    def pos_lemma(self, text):
        lemma = []
        pos = []
        doc = self.nlp(text, disable=['parser', 'ner'])
        for sent in doc.sents:
            for token in sent:
                lemma.append(token.lemma_)
                pos.append(token.tag_)
        return pos, lemma

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

    def custom_tokenizer(self, text):
        seg_text = []
        for sentence in self.tokenizer(text)[0]:
            for token in sentence:
                seg_text.append(token)
            seg_text.append('\n')
        if seg_text[-1] == '\n':
            seg_text.pop(-1)
        return Doc(self.nlp.vocab, seg_text)
