class MetaFeatures:

    def __init__(self):
        self.functions = {
                         'is_retweet' : self.is_retweet,
                         'is_quote' : self.is_quote,
                         'is_original_author' : self.is_original_author,
                         'is_truncated' : self.is_truncated,
                         'is_reply' : self.is_reply
                         }

    def feature_occurences(self, tweet):
        results = {}
        for func in self.functions:
            results[func] = self.functions[func](tweet)
        return results

    def is_retweet(self, tweet):
        if tweet.is_retweet == True:
            return 1
        else:
            return 0

    def is_quote(self, tweet):
        if tweet.is_quote_status == True:
            return 1
        else:
            return 0

    def is_original_author(self, tweet):
        if isinstance(tweet.original_author, str):
            return 1
        else:
            return 0

    def is_truncated(self, tweet):
        if tweet.truncated == True:
            return 1
        else:
            return 0

    def is_reply(self, tweet):
        if isinstance(tweet.in_reply_to_screen_name, str):
            return 1
        else:
            return 0
