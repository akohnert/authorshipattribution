from collections import Counter


class WordFeatures:

    def __init__(self):
        self.functions = {
                         'token num': self.token_num,
                         'avg. token length': self.avg_token_length,
                         'token types': self.token_types,
                         'string types': self.string_types
                         }
        self.str_functions = {
                             'uppercase tokens': str.isupper,
                             'numeric tokens': str.isnumeric,
                             'alphabet-only tokens': str.isalpha
                             }
        self.token_types = ['hashtag', 'URL', 'mention', 'emoticon','symbol']
        self.num_tokens = 0

    def feature_occurences(self, preprocessed_text):
        results = {}
        for func in self.functions:
            feature = self.functions[func](preprocessed_text)
            if isinstance(feature, float):
                results[func] = self.functions[func](preprocessed_text)
            if isinstance(feature, Counter):
                results = {**results, **feature}
        return results

    def token_num(self, preprocessed_text):
        tokens = [len(sentence) for sentence in preprocessed_text['tokens']]
        self.num_tokens = sum(tokens)
        return self.num_tokens

    def token_types(self, preprocessed_text):
        c = Counter()
        for type in self.token_types:
            c[type] = preprocessed_text['types'].count(type) / self.num_tokens
        return c

    def string_types(self, preprocessed_text):
        c = Counter()
        for func in self.str_functions:
            for sentence in preprocessed_text['tokens']:
                for token in sentence:
                    c[func] += int(self.str_functions[func](token))
            c[func] /= self.num_tokens
        return c

    def avg_token_length(self, preprocessed_text):
        char_sum = 0
        for sentence in preprocessed_text['tokens']:
            char_sum += sum(len(token) for token in sentence)
        return char_sum / self.num_tokens
