from sklearn.model_selection import train_test_split
from Scripts.App_log import logger


class modeler():
    
    def __init__(self) -> None:
        pass
    
        logger.info("successfully initialized modeler class")
        
        
        
    def dependent_variable(self,df,target):
        """
        --separate dependent and indepentent features
        """
        independent_features = df[df.columns.difference([target])]
        
        dependent_variable = df[[target]]
        
        logger.info("successful separate the dataset")
        
        return independent_features, dependent_variable 
    
    
    def split_data(self,df,target):
        """
        -- spliting the data
        """
        
        X,y = self.dependent_variable(df,target)
        
        X_train,X_test,y_train,y_test = train_test_split(X,y,test_size=0.1,random_state=42)
        X_train,X_val,y_train,y_val = train_test_split(X_train,y_train,test_size=0.2,random_state = 42)
        
        logger.info("Successful split the data")
        
        return X_train, X_test, X_val, y_train, y_test,y_val
    
   
    