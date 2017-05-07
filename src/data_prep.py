import pandas as pd
#from pymongo import MongoClient

def load_raw_data(filename):
    '''load data to a pandas df'''
    df = pd.read_csv(filename)
    return df

def construct_basic_fake_df(df):
    '''strips down original fake news dataset
    and return text, and label
    ''' 
    df = df[['text', 'type']]
    return df    

def raw_data_cleaner():
    #return X
    pass

if __name__ == '__main__':
    data = load_raw_data('data/fake.csv')
    fake_df = construct_basic_fake_df(data)
    print 'cleaning data'
