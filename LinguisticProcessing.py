from somajo import SoMaJo
import spacy
import en_core_web_sm
from spacy.tokens import Doc
from spacy.pipeline import SentenceSegmenter

class LinguisticProcessing:

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
            t = []
            for token in sent:
                sentences.append(token.text)
                t.append(token.token_class)
            sentences.append('\n')
            types.append(t)
        return sentences, types


    def spacy(self, text):
        lemma = []
        pos = []
        doc = self.nlp(text, disable=['parser', 'ner'])
        for sent in doc.sents:
            for token in sent:
                lemma.append(token.lemma_)
                pos.append(token.tag_)
        print(lemma, pos)
        return lemma, pos


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
        if text[-1] == '\n':
            text.pop(-1)
        return Doc(self.nlp.vocab, text)

if __name__ == '__main__':
    l = LinguisticProcessing('hillary_trump_tweets.csv')
