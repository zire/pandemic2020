import numpy as np 
import pandas as pd 
import matplotlib.pyplot as plt
import matplotlib.dates as mdates

df = pd.read_csv(
	'../data/pandemic2020.csv',
	dtype={
		'Close Contact': 'float',
		'In Treatment': 'float',
		'Suspected Infection': 'float',
		'Confirmed Infection': 'float',
		'Severe Infection': 'float',
		'Death': 'float',
		'Cured': 'float'
		}
	)
df['Date'] = pd.to_datetime(df['Date'])

# print(df)
# print(df.dtypes)

df['Close Contact New'] = df['Close Contact'].diff()
df['In Treatment New'] = df['In Treatment'].diff()
df['Suspected Infection New'] = df['Suspected Infection'].diff()
df['Confirmed Infection New'] = df['Confirmed Infection'].diff()
df['Severe Infection New'] = df['Severe Infection'].diff()
df['Death New'] = df['Death'].diff()
df['Cured New'] = df['Cured'].diff()

# print(df)

# print(df.dtypes)

plt.rcParams["font.family"]= "Heiti TC"

# m: magenta, b: blue, c: cyan, r: red

# ------------ Plot Life-To-Date Chart for the Big 4 --------------------------

fig = df.plot(
	x='Date', 
	y=['Suspected Infection', 'Confirmed Infection', 'Severe Infection','Death'],
	style=['m', 'b', 'c', 'r'],
	linewidth=3
)
plt.title('2020年新型冠状病毒感染趋势图 - 累计数据')
plt.xlabel('日期')
plt.ylabel('累计人数')
# fig.xaxis.set_major_locator(mdates.DayLocator(interval=1))
# fig.xaxis.set_major_formatter(mdates.DateFormatter('%m/%d'))
# plt.show()
plt.savefig('../charts/chart_big_4_ltd.png')
print('chart_big_4_ltd updated!')
plt.close()

# ------------ Plot Daily Net New Chart for the Big 4 -------------------------

df.plot(
	x='Date', 
	y=['Suspected Infection New', 'Confirmed Infection New', 'Severe Infection New','Death New'],
	style=['m', 'b', 'c', 'r'],
	linewidth=3
)
plt.title('2020年新型冠状病毒感染趋势图 - 每日新增')
plt.xlabel('日期')
plt.ylabel('新增人数')
# fig.xaxis.set_major_locator(mdates.DayLocator(interval=2))
# fig.xaxis.set_major_formatter(mdates.DateFormatter('%m-%d'))
# plt.show()
plt.savefig('../charts/chart_big_4_net_new.png')
print('chart_big_4_net_new updated!')
plt.close()

# ------------ Plot Life-to-Date for Death and Cured --------------------------

df.plot(
	x='Date', 
	y=['Death', 'Cured'],
	style=['r', 'g'],
	linewidth=3
)
plt.title('2020年新型冠状病毒感染趋势图 - 死亡和治愈')
plt.xlabel('日期')
plt.ylabel('累计人数')
# fig.xaxis.set_major_locator(mdates.DayLocator(interval=3))
# fig.xaxis.set_major_formatter(mdates.DateFormatter('%m%d'))
# plt.show()
plt.savefig('../charts/chart_DnC_LTD.png')
print('chart_DnC_LTD updated!')
plt.close()




