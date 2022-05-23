import matplotlib.pyplot as plt
import seaborn as sns

class Data_visualiz:
    
    def __init__(self):
        """
        initializing data_visualiz class
        """
        
    def boxplot(df,column):
        sns.boxplot(x = df[column])
        plt.title(f"boxplot of {column}")
        plt.ylabel("values")
        plt.show()