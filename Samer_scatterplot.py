import pandas as pd           # to read csv files and plot the data
import numpy as np
import matplotlib.pyplot as plt


data = pd.read_csv('weeks.csv')   #reads csv file that has info

X = data.iloc[:, 0]    # reads the file variables found from FileTouches script
Y = data.iloc[:, 1]     # reads column of amount of weeks

plt.scatter(X, Y, c=Y, s=100, cmap='blue')    # create scatter plot
plt.show()   #prints plot