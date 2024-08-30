import pandas as pd
from matplotlib import pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
import seaborn as sns
def marks(marks):
    ram = pd.read_csv('placement.csv')
    x = ram[['cgpa']]
    y = ram['package']
    x_train,x_test,y_train,y_test = train_test_split(x,y,test_size=0.2,random_state=42)
    lr = LinearRegression()
    lr.fit(x_train,y_train)
    return lr.predict([[marks]])



