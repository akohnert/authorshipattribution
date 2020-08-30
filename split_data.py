import pandas as pd
import random
import sys
from os.path import isdir


class Split:
    def __init__(self, input):
        self.data = pd.read_csv(input, encoding='utf-8')

    def split_train_test_dev(self):
        train = []
        test = []
        dev = []
        # 70% Training, 20% Test, 10% Validierung
        # gleich Anteile von allen Autoren pro Set
        for handle in self.data.handle.unique():
            x = self.data.index[self.data.handle == handle].tolist()
            train_instances = round(len(x) / 100 * 70)
            train.append(random.sample(x, train_instances))
            y = list(set(x) - set(train[-1]))
            test_instances = round(len(x) / 100 * 20)
            test.append(random.sample(y, test_instances))
            z = list(set(y) - set(test[-1]))
            dev.append(z)

        # Testen, ob alle Instanzen richtig verteilt wurden
        all_instances = set(train[0]+train[1]+test[0]+test[1]+dev[0]+dev[1])
        assert(len(all_instances) == self.data.shape[0])

        train = train[0]+train[1]
        test = test[0]+test[1]
        dev = dev[0]+dev[1]

        return train, test, dev

    def to_file(self, train_str="", test_str="", dev_str="", dir=""):
        train, test, dev = self.split_train_test_dev()
        if train_str == "":
            train_str = 'train_set.csv'
        if test_str == "":
            test_str = 'test_set.csv'
        if dev_str == "":
            dev_str = "dev_set.csv"
        if dir != "" and dir[-1] != "/":
            dir += "/"

        train_set = self.data.drop(self.data.index[test+dev])
        test_set = self.data.drop(self.data.index[train+dev])
        dev_set = self.data.drop(self.data.index[test+train])

        train_set.to_csv(dir+train_str, encoding="utf-8")
        test_set.to_csv(dir+test_str, encoding="utf-8")
        dev_set.to_csv(dir+dev_str, encoding="utf-8")


if __name__ == "__main__":
    if len(sys.argv) not in [2, 3]:
        print('usage: split_data.py DATA_SET [OUTPUT_PATH]')
        sys.exit()
    output_path = ""
    if len(sys.argv) == 3:
        output_path = sys.argv[2]
        if not isdir(output_path):
            mkdir(output_path)
    Split(sys.argv[1]).to_file(dir=output_path)
