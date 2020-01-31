import numpy as np 
import pandas as pd 
import matplotlib.pyplot as plt
import matplotlib.dates as mdates

lifeToDate = pd.read_csv('../data/pandemic2020.csv')

netNew = lifeToDate.set_index('Date').diff()
# print(netNew)

plt.rcParams["font.family"]= "Heiti TC"

# m: magenta, b: blue, c: cyan, r: red


# set daily locator
# chart.xaxis.set_major_locator(mdates.DayLocator(interval=1))
# chart.xaxis.set_major_formatter(mdates.DateFormatter('%d-%m'))

chartLTD = lifeToDate.plot(
	x='Date', 
	y=['Suspected Infection', 'Confirmed Infection', 'Severe Infection','Death'],
	style=['m', 'b', 'c', 'r'],
	linewidth=3
)
plt.title('2020年新型冠状病毒感染趋势图 - 累计数据')
plt.xlabel('日期')
plt.ylabel('累计人数')
# plt.show()
plt.savefig('../charts/chart_big_4_ltd.png')
plt.close()

# chartNW = netNew.plot(
# 	x='Date', 
# 	y=['Suspected Infection', 'Confirmed Infection', 'Severe Infection','Death'],
# 	style=['m', 'b', 'c', 'r'],
# 	linewidth=3
# )
# plt.title('2020年新型冠状病毒感染趋势图 - 每日新增数据')
# plt.xlabel('日期')
# plt.ylabel('新增人数')
# plt.show()
# plt.savefig('../charts/chart_big_4_net_new.png')