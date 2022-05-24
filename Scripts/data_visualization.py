import matplotlib.pyplot as plt
import seaborn as sns
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