class WordFeatures:

    def __init__(self):
        self.functions = [
                         self.number,
                         self.avg_length,
                         self.emoticons,
                         self.hashtags,
                         self.mentions,
                         ]

    def ignore_segmentation(self, tokens):
        words = []
        types = []
        for i, sentence in enumerate(tokens[0]):
            for j, token in enumerate(sentence):
                words.append(token)
                types.append(tokens[1][i][j])
        return words, types

    def feature_occurences(self, tokens):
        tokens = self.ignore_segmentation(tokens)
        results = []
        for func in self.functions:
            results.append(func(tokens))
        return results


    def number(self, tokens):
        return len(tokens[0])

    def emoticons(self, tokens):
        return tokens[1].count('emoticon') / self.number(tokens)

    def hashtags(self, tokens):
        return tokens[1].count('hashtag') / self.number(tokens)

    def mentions(self, tokens):
        return tokens[1].count('mention') / self.number(tokens)

    def avg_length(self, tokens):
        all_token_chars = sum(len(token) for token in tokens[0])
        return all_token_chars / self.number(tokens)

    #def OOV_words(self, tokens):
    #    OOV = 0
    #    for token in tokens[0]:
