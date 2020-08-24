class SentenceFeatures:

    def __init__(self):
        self.functions = [
                         self.number,
                         self.chars_per_sentence,
                         self.tokens_per_sentence
                         ]

    def number(self, tokens):
        return (len(tokens[0]))

    def chars_per_sentence(self, tokens):
        chars = 0
        for sentence in tokens[0]:
            chars += sum(len(token) for token in sentence)
        return chars / self.number(tokens)

    def tokens_per_sentence(self, tokens):
        token_num = sum(len(sentence) in  tokens[0])
        return token_num / self.number(tokens)
