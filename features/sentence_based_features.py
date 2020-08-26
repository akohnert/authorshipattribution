from LinguisticPreprocessing import Preprocessing
# Zu aufwändig, nicht jedes Mal Tokenizer rufen

class SentenceFeatures:

    def __init__(self):
        self.functions = {
                         'Number sentences' : self.number,
                         'chars per sentence' : self.chars_per_sentence,
                         'tokens per sentence' : self.tokens_per_sentence
                         }

    def feature_occurences(self, text):
        results = {}
        for func in self.functions:
            results[func] = self.functions[func](text)
        return results

    def get_tokens(self, text):
        tokens = Preprocessing().tokenizer(text)
        return tokens

    def number(self, text):
        tokens = self.get_tokens(text)
        return len(tokens[0])

    def chars_per_sentence(self, text):
        tokens = self.get_tokens(text)
        chars = 0
        for sentence in tokens[0]:
            chars += sum(len(token) for token in sentence)
        return chars / self.number(text)

    def tokens_per_sentence(self, text):
        tokens = self.get_tokens(text)
        token_num = sum(len(sentence) for sentence in tokens[0])
        return token_num / self.number(text)
