import pandas as pd
from extract_features import FeatureExtraction

def main():
    data = pd.read_csv('../dev_set.csv')
    for i, tweet in data.iterrows():
        print(i)
        output = FeatureExtraction(tweet).all_features()
        #print(tweet.text)
        #print(output)



if __name__ == '__main__':
    main()
