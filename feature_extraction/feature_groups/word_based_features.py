class WordFeatures:

    def __init__(self):
        self.functions = {
                         'Tokens per Tweet': self.tokens,
                         'Avg. token length': self.avg_token_length,
                         'Emoticons per Tweet': self.emoticons,
                         'Hashtags per Tweet': self.hashtags,
                         'Mentions per Tweet': self.mentions,
                         'URLs per Tweet': self.urls
                         }
        self.len_tokens = 0

    def feature_occurences(self, preprocessed_text):
        results = {}
        for func in self.functions:
            results[func] = self.functions[func](preprocessed_text)
        return results

    def tokens(self, preprocessed_text):
        self.len_tokens = len(preprocessed_text['tokens'])
        return self.len_tokens

    def emoticons(self, preprocessed_text):
        return preprocessed_text['types'].count('emoticon') / self.len_tokens

    def hashtags(self, preprocessed_text):
        return preprocessed_text['types'].count('hashtag') / self.len_tokens

    def mentions(self, preprocessed_text):
        return preprocessed_text['types'].count('mention') / self.len_tokens

    def urls(self, preprocessed_text):
        return preprocessed_text['types'].count('URL') / self.len_tokens

    def avg_token_length(self, preprocessed_text):
        tok_length = sum(len(token) for token in preprocessed_text['tokens'])
        return tok_length / self.len_tokens
