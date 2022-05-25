import matplotlib.pyplot as plt
import seaborn as sns
import matplotlib as mpl
mpl.rcParams['agg.path.chunksize'] = 10000
from Scripts.Data_cleaning import load_data,clean_data
sns.set()

class Data_visualiz:
    
    def __init__(self):
        """
        initializing data_visualiz class
        """
     #plot boxplot    
    def boxplot(self,df,column):
        sns.boxplot(x = df[column])
        plt.title(f"boxplot of {column}")
        plt.ylabel("values")
        plt.show()
        
     #plot histograms  
    def histogram(self,df):
        num_cols = df.select_dtypes(include=['int64','float64']).columns.tolist()
        df[num_cols].hist(figsize=(20,20))
    
    def plot(self,df,col,col1):
        plt.figure(figsize=(10,8))
        plt.plot(df[col],df[col1])
        plt.title(f'Time serie of {col1}')
        plt.xlabel('Date')
        plt.ylabel('Sales')
        
    def plot_counts(self,df,col1,col2=None,Type=None,**kwargs):
        
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
            plt.title(f"Scatter plot of {col2} against {col2}")
         
        elif Type == 'bar':
            plt.figure(figsize=(10,8))
            sns.barplot(x=col1, y=col2, data=df)
            plt.title(f"{col2} in {col1}")
            plt.show()
            
    