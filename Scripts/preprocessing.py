import pandas as pd 
import numpy as np 
from Scripts.App_log import logger 


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
        