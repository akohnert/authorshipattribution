from feature_extraction.feature_groups.FeatureBaseClass import Features


class MetaFeatures(Features):

    def __init__(self):
        self.functions = {
                         'is_retweet': self.is_retweet,
                         'is_quote': self.is_quote,
                         'is_original_author': self.is_original_author,
                         'is_truncated': self.is_truncated,
                         'is_reply': self.is_reply
                         }

    def feature_occurences(self, tweet):
        results = {}
        for func in self.functions:
            results[func] = self.functions[func](tweet)
        return results

    def is_retweet(self, tweet):
        return int(tweet.is_retweet)

    def is_quote(self, tweet):
        return int(tweet.is_quote_status)

    def is_original_author(self, tweet):
        return int(isinstance(tweet.original_author, str))

    def is_truncated(self, tweet):
        return int(tweet.truncated)

    def is_reply(self, tweet):
        return int(isinstance(tweet.in_reply_to_screen_name, str))
