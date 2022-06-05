import matplotlib.pyplot as plt
import seaborn as sns
import matplotlib as mpl
mpl.rcParams['agg.path.chunksize'] = 10000
from Scripts.Data_cleaning import load_data,clean_data
from Scripts.App_log import logger 
sns.set()

class Data_visualiz:
    
    def __init__(self):
        """
        initializing data_visualiz class
        """
        logger.info('Successfull initialize data visualiz class')
     #plot boxplot    
    def plot_boxplot(self,df,col):
        plt.boxplot(x = df[col])
        plt.title(f"boxplot of {col}")
        plt.ylabel("values")
        plt.show()
        logger.info('Plotted boxplot')
        
     #plot histograms  
    def histogram(self,df):
        num_cols = df.select_dtypes(include=['int64','float64']).columns.tolist()
        df[num_cols].hist(figsize=(20,20))
        logger.info('plotted histogram')
    
    def plot(self,df,col,col1):
        plt.figure(figsize=(10,8))
        plt.plot(df[col],df[col1])
        plt.title(f'Time serie of {col1}')
        plt.xlabel('Date')
        plt.ylabel('Sales')
        logger.info('plotted time series')
        
    def plot_counts(self,df,col1,col2=None,col3=None,Type=None,**kwargs):
        
        if Type=='univariate':
            plt.figure(figsize=(8,6))
            sns.countplot(data=df,x=col1)
            plt.title(f"unique value counts of the {col1}")
            plt.show()
            
        elif Type == 'bivariate_scatter':
            plt.figure(figsize=(8,6))
            plt.scatter(df[col1],df[col2])
            plt.xlabel(col1)
            plt.ylabel(col2)
            plt.title(f"Scatter plot of {col1} against {col2}")
            plt.show()
         
        elif Type == 'bar':
            plt.figure(figsize=(10,8))
            sns.barplot(x=col1, y=col2, data=df)
            plt.title(f"{col2} in {col1}")
            plt.show()
            
        elif Type == 'lineplot':
            plt.figure(figsize=(10,8))
            sns.lineplot(df[col1], y= df[col2], hue=df[col3],ci=None)
            plt.show()
            
        elif Type == 'boxplot':
            plt.boxplot(x = df[col1])
            plt.title(f"boxplot of {col1}")
            plt.ylabel("values")
            plt.show()

            logger.info('plotted plot counts')
            ## return 

            
    