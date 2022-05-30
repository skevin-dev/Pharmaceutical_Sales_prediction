import pandas as pd 
import numpy as np 
from Scripts.App_log import logger 
from sklearn.preprocessing import StandardScaler,MinMaxScaler


class preprocess(): 
    
    def __init__(self,df):
    
        """
        initializing the preprocess class
        """
        self.df = df 
        logger.info('successful initialize the class')
        
    def label_encoder(self,df:pd.DataFrame)->pd.DataFrame:
        categorical_features = self.df.select_dtypes(include='object').columns.tolist()
        
        for i in categorical_features:
            self.df[categorical_features] = self.df[categorical_features].apply(lambda x: pd.factorize(x)[0])
            
        logger.info('successful convert to numeric')
        
        
    def scalling_data(self,df:pd.DataFrame)->pd.DataFrame:
        scaler = MinMaxScaler()
        df[:] = scaler.fit_transform(df[:])
        logger.info("successful scaling data")
        