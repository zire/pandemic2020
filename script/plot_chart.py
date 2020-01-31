import numpy as np 
import pandas as pd 
import matplotlib.pyplot as plt
import time
from datetime import datetime

df = pd.read_csv('../data/pandemic2020.csv')

print(df.columns)
# print(df.index)

# xAxis = df.Date.strftime('%m/%d')

xAxis = df.Date

# print(xAxis)

yAxis_1 = df.Death
yAxis_2 = df.Cured

# print(yAxis)

plt.plot(xAxis,yAxis_1,yAxis_2)
plt.title('Total Death')
plt.xlabel('Date')
plt.ylabel('Number')
plt.show()
