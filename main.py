import pandas as pd
from extract_features import FeatureExtraction
from data_set_features import DataSetFeatures

def main():
    f = DataSetFeaturesFeatures('../dev_set.csv')
    f.save_features('dev_set_features.csv')
    f.aggregate_features('dev_set_features_aggregated.csv')
    #data = pd.read_csv('../dev_set.csv')
    #for i, tweet in data.iterrows():
    #    output = FeatureExtraction(tweet).all_features()
    #    print(output)



if __name__ == '__main__':
    main()
