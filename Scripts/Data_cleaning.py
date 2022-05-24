import pandas as pd 
import numpy as np 

def load_data(filepath):
    df = pd.read_csv(filepath)
    return df 

class clean_data():
    def __init__(self,df):
        self.df = df
    
    def descriptive_statistics(self,info=False,shape=False,describe=False,missing_values=False):
        information=None
        if info:
            information = self.df.info()
        elif shape:
            information = self.df.shape
        elif describe:
            information = self.df.describe()
        elif missing_values:
            information = self.df.isna().sum()
        
        return information
    
    def fix_outliers(self,df,column):
        df[column] = np.where(df[column] > df[column].quantile(0.95), df[column].median(),df[column])
    
        return df[column]