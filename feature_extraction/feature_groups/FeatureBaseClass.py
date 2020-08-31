from abc import ABC, abstractmethod

class Features(ABC):

    @abstractmethod
    def __init__(self):
        pass

    @abstractmethod
    def feature_occurences(self):
        # (kein wirklicher Effekt) Rückgabetype ist Dictionary/Counter
        return {}
