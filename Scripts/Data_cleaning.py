import pandas as pd 
import numpy as np 

def load_data(filepath):
    df = pd.read_csv(filepath)
    return df 

class clean_data():
    def __init__(self,df):
        self.df = df
        
    #perform descriptive statistics
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
    
    #fixing outliers 
    def fix_outliers(self,df,column):
        df[column] = np.where(df[column] > df[column].quantile(0.95), df[column].median(),df[column])
    
        return df[column]
    
    #converting columns to string
    def convert_to_string(self,df, columns):
        for col in columns:
            df[col] = df[col].astype("string")
            
    #converting column to int
    def convert_to_int(self,df, columns):
        for col in columns:
            df[col] = df[col].astype("int64")
            
    #converting column to datetime
    def convert_to_datetime(self,df, columns):
        for col in columns:
            df[col] = pd.to_datetime(df[col])
    
    #handling categorial and numeric columns by filling with mean and median and model
    def handling_missing(self,df):
        
        #numeric column
        df_num = df.select_dtypes(include=["float","int"])
        normal_dist = []
        skewed = []
        for i in df_num.columns:
            #checking for skewness
            if df_num[i].skew() < 0.5 and df_num[i].skew() > -0.5:
                normal_dist.append(i)
            else:
                skewed.append(i)
         # for normal distribution values fill with median
        for t in normal_dist:
            df[t].fillna(df[t].median(),inplace=True)
          # for skewed fill with mean
        for j in skewed:
            df[j].fillna(df[j].mean(),inplace=True)
        
        #for categorical fill with model
        df_cat = df.select_dtypes(include=["object"])
        for n in df_cat.columns:
            df[n].fillna(df[n].mode()[0],inplace=True)
     
     #fill nan values with values       
    def filling_nan(self,df, cols, value):
        for col in cols:
            df[col].fillna(value,inplace=True)
       
    # unique values in columns
    def unique_values(self,df,column):
        unique_values = df[column].unique()
        return unique_values
    
    #drop duplicate
    def drop_duplicate(self,df,column):
        df = df.drop_duplicates(subset=[column])
        return df 
    
    # merge datasets 
    def merge(df,df1,column):
        df_merged = pd.merge(df,df1,how="left",on=column)
        return df_merged
    
    
    