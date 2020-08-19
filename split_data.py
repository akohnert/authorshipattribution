import pandas as pd
import random


class Split:

    def __init__(self, input):
        self.data = pd.read_csv(input, encoding='utf-8')
        print(self.data.shape)

    def split_train_test_dev(self):
        train = []
        test = []
        dev = []
        for handle in self.data.handle.unique():
            x = self.data.index[self.data.handle == handle].tolist()
            train_instances = round(len(x) / 100 * 70)
            train.append(random.sample(x, train_instances))
            y = list(set(x) - set(train[-1]))
            test_instances = round(len(x) / 100 * 20)
            test.append(random.sample(y, test_instances))
            z = list(set(y) - set(test[-1]))
            dev.append(z)

        assert(len(train[0])+len(train[1])+len(test[0])+len(test[1])+len(dev[0])+len(dev[1]) == self.data.shape[0])
        assert(len(set(train[0]+train[1]+test[0]+test[1]+dev[0]+dev[1])) == self.data.shape[0])

        train = train[0]+train[1]
        test = test[0]+test[1]
        dev = dev[0]+dev[1]

        return train, test, dev

    def to_file(self, train_str="", test_str="", dev_str=""):
        train, test, dev = self.split_train_test_dev()
        if train_str == "":
            train_str = 'train_set.csv'
        if test_str == "":
            test_str = 'test_set.csv'
        if dev_str == "":
            dev_str = "dev_set.csv"

        train_set = self.data.drop(self.data.index[test+dev])
        test_set = self.data.drop(self.data.index[train+dev])
        dev_set = self.data.drop(self.data.index[test+train])

        train_set.to_csv(train_str, encoding="utf-8")
        test_set.to_csv(test_str, encoding="utf-8")
        dev_set.to_csv(dev_str, encoding="utf-8")
