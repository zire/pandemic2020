import numpy as np 
import pandas as pd 
import matplotlib.pyplot as plt
import matplotlib.dates as mdates

df = pd.read_csv(
	'../data/pandemic2020.csv',
	dtype={
		'接触': 'float',
		'观察': 'float',
		'疑似': 'float',
		'确诊': 'float',
		'重症': 'float',
		'死亡': 'float',
		'治愈': 'float'
		}
	)
df['日期'] = pd.to_datetime(df['日期'])

# print(df)
# print(df.dtypes)

df['接触_新'] = df['接触'].diff()
df['观察_新'] = df['观察'].diff()
df['疑似_新'] = df['疑似'].diff()
df['确诊_新'] = df['确诊'].diff()
df['重症_新'] = df['重症'].diff()
df['死亡_新'] = df['死亡'].diff()
df['治愈_新'] = df['治愈'].diff()

# print(df)

# print(df.dtypes)

plt.rcParams["font.family"]= "Heiti TC"

# m: magenta, b: blue, c: cyan, r: red

# ------------ Plot Life-To-Date Chart for the Big 4 --------------------------

fig = df.plot(
	x='日期', 
	y=['疑似', '确诊', '重症','死亡'],
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
	x='日期', 
	y=['疑似_新', '确诊_新', '重症_新','死亡_新'],
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
	x='日期', 
	y=['死亡', '治愈'],
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




