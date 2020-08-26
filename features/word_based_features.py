from LinguisticPreprocessing import Preprocessing
# Zu aufwändig, nciht jedes Mal Tokenizer rufen


class WordFeatures:

    def __init__(self):
        self.functions = {
                         'Tokens per Tweet' : self.tokens,
                         'Avg. token length' : self.avg_token_length,
                         'Emoticons per Tweet' : self.emoticons,
                         'Hashtags per Tweet' :self.hashtags,
                         'Mentions per Tweet' :self.mentions,
                         'URLs per Tweet' : self.urls
                         }

    def get_tokens(self, text):
        tokens = Preprocessing().tokenizer(text)
        words = []
        types = []
        for i, sentence in enumerate(tokens[0]):
            for j, token in enumerate(sentence):
                words.append(token)
                types.append(tokens[1][i][j])
        return words, types

    def feature_occurences(self, text):
        tokens = self.get_tokens(text)
        results = {}
        for func in self.functions:
            results[func] = self.functions[func](tokens)
        return results

    def tokens(self, tokens):
        return len(tokens[0])

    def emoticons(self, tokens):
        return tokens[1].count('emoticon') / len(tokens[0])

    def hashtags(self, tokens):
        return tokens[1].count('hashtag') / len(tokens[0])

    def mentions(self, tokens):
        return tokens[1].count('mention') / len(tokens[0])

    def urls(self, tokens):
        return tokens[1].count('URL') / len(tokens[0])

    def avg_token_length(self, tokens):
        all_token_chars = sum(len(token) for token in tokens[0])
        return all_token_chars / len(tokens[0])

    #def OOV_words(self, tokens):
    #    OOV = 0
    #    for token in tokens[0]:
