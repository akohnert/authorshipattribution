class WordFeatures:

    def __init__(self):
        self.functions = [
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


    def emoticons(self, tokens):
        return tokens[1].count('emoticon') / len(tokens[0])

    def hashtags(self, tokens):
        return tokens[1].count('hashtag') / len(tokens[0])

    def mentions(self, tokens):
        return tokens[1].count('mention') / len(tokens[0])

    def avg_length(self, tokens):
        all_token_chars = sum(len(token) for token in tokens[0])
        return all_token_chars / len(tokens[0])

    #def OOV_words(self, tokens):
    #    OOV = 0
    #    for token in tokens[0]:
