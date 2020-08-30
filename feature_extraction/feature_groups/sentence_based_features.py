class SentenceFeatures:

    def __init__(self):
        self.functions = {
                         'Number sentences': self.number,
                         'chars per sentence': self.chars_per_sentence,
                         'tokens per sentence': self.tokens_per_sentence
                         }

    def feature_occurences(self, preprocessed_text):
        results = {}
        for func in self.functions:
            results[func] = self.functions[func](preprocessed_text)
        return results

    def number(self, preprocessed_text):
        return len(preprocessed_text['tokens'])

    def chars_per_sentence(self, preprocessed_text):
        chars = 0
        for sentence in preprocessed_text['tokens']:
            chars += sum(len(token) for token in sentence)
        return chars / self.number(preprocessed_text)

    def tokens_per_sentence(self, preprocessed_text):
        num = sum(len(sentence) for sentence in preprocessed_text['tokens'])
        return num / self.number(preprocessed_text)
