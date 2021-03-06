import numpy as np 
import pandas as pd 
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
from tabulate import tabulate
from datetime import timedelta

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

# Create new columns for daily incremental

df['接触_新增量'] = df['接触'].diff()
df['观察_新增量'] = df['观察'].diff()
df['疑似_新增量'] = df['疑似'].diff()
df['确诊_新增量'] = df['确诊'].diff()
df['重症_新增量'] = df['重症'].diff()
df['死亡_新增量'] = df['死亡'].diff()
df['治愈_新增量'] = df['治愈'].diff()

# Create new columns for daily change percentage

df['接触_新增率'] = df['接触'].pct_change()
df['观察_新增率'] = df['观察'].pct_change()
df['疑似_新增率'] = df['疑似'].pct_change()
df['确诊_新增率'] = df['确诊'].pct_change()
df['重症_新增率'] = df['重症'].pct_change()
df['死亡_新增率'] = df['死亡'].pct_change()
df['治愈_新增率'] = df['治愈'].pct_change()

# pd.options.display.float_format = '{:,}'.format

# print(df)

# print(df.dtypes)

plt.rcParams["font.family"]= "Heiti TC"

# m: magenta, b: blue, c: cyan, r: red

# ------------ Plot Life-To-Date Chart for the Big 5 --------------------------

fig = df.plot(
	x='日期', 
	y=['疑似', '确诊', '重症','死亡', '治愈'],
	style=['m', 'b', 'c', 'r', 'g'],
	linewidth=3
)
plt.title('疑似，确诊，重症，死亡，治愈 - 累计数据')
plt.xlabel('日期')
plt.ylabel('累计人数')
# fig.xaxis.set_major_locator(mdates.DayLocator(interval=1))
# fig.xaxis.set_major_formatter(mdates.DateFormatter('%m/%d'))
# plt.show()
plt.savefig('../charts/chart_big_5_ltd.png')
print('chart_big_5_ltd updated!')
plt.close()

# ------------ Plot Daily Net New Chart for 疑似 and 确诊 -------------------------

df.plot(
	x='日期', 
	y=['疑似_新增量', '确诊_新增量'],
	style=['m', 'b'],
	linewidth=3
)
plt.title('疑似，确诊 - 每日新增')
plt.xlabel('日期')
plt.ylabel('新增人数')
# fig.xaxis.set_major_locator(mdates.DayLocator(interval=2))
# fig.xaxis.set_major_formatter(mdates.DateFormatter('%m-%d'))
# plt.show()
plt.savefig('../charts/chart_big_2_net_new.png')
print('chart_big_2_net_new updated!')
plt.close()

# ------------ Plot Daily Net New for Death and Cured --------------------------

df.plot(
	x='日期', 
	y=['死亡_新增量', '治愈_新增量'],
	style=['r', 'g'],
	linewidth=3
)
plt.title('死亡，治愈 - 每日新增')
plt.xlabel('日期')
plt.ylabel('新增人数')
# fig.xaxis.set_major_locator(mdates.DayLocator(interval=3))
# fig.xaxis.set_major_formatter(mdates.DateFormatter('%m%d'))
# plt.show()
plt.savefig('../charts/chart_DnC_net_new.png')
print('chart_DnC_net_new updated!')
plt.close()

# ----------- Create README.md ------------------------------------------------

current_date = df['日期'].iat[-1] + timedelta(days=1)

df_ltd = df[['日期', '接触', '观察', '疑似', '确诊', '重症', '死亡', '治愈', 'Source']].iloc[::-1]

# print(df_ltd['日期'])

# df_ltd['日期'] = pd.to_datetime(df_ltd['日期'], format="%m/%d")

# print(df_ltd['日期'].strftime('%m/%d'))

df_ltd['日期'] = df_ltd['日期'].map('{:%m/%d}'.format)
df_ltd['日期'] = df_ltd[['日期','Source']].apply(lambda row: "<a href='%s'>%s</a>" % (row['Source'], row['日期']), axis=1)
# df_ltd['日期'] = df_ltd['日期'].map('{:%m/%d}'.format)
df_ltd['接触'] = df_ltd['接触'].map('{:,.0f}'.format)
df_ltd['观察'] = df_ltd['观察'].map('{:,.0f}'.format)
df_ltd['疑似'] = df_ltd['疑似'].map('{:,.0f}'.format)
df_ltd['确诊'] = df_ltd['确诊'].map('{:,.0f}'.format)
df_ltd['重症'] = df_ltd['重症'].map('{:,.0f}'.format)
df_ltd['死亡'] = df_ltd['死亡'].map('{:,.0f}'.format)
df_ltd['治愈'] = df_ltd['治愈'].map('{:,.0f}'.format)

ltd_table = tabulate(
	df_ltd.loc[:,df_ltd.columns != 'Source'],
	headers = ['日期', '接触', '观察', '疑似', '确诊', '重症', '死亡', '治愈'],
	showindex = 'always',
	tablefmt = 'pipe',
	stralign = 'right'
)

# print(ltd_table)

df_new = df[[
	'日期', '接触_新增量', '观察_新增量', '疑似_新增量', '确诊_新增量', '重症_新增量', '死亡_新增量', '治愈_新增量', 'Source'
	]].iloc[::-1]

df_new['日期'] = df_new['日期'].map('{:%m/%d}'.format)
df_new['日期'] = df_new[['日期','Source']].apply(lambda row: "<a href='%s'>%s</a>" % (row['Source'], row['日期']), axis=1)
df_new['接触_新增量'] = df_new['接触_新增量'].map('{:,.0f}'.format)
df_new['观察_新增量'] = df_new['观察_新增量'].map('{:,.0f}'.format)
df_new['疑似_新增量'] = df_new['疑似_新增量'].map('{:,.0f}'.format)
df_new['确诊_新增量'] = df_new['确诊_新增量'].map('{:,.0f}'.format)
df_new['重症_新增量'] = df_new['重症_新增量'].map('{:,.0f}'.format)
df_new['死亡_新增量'] = df_new['死亡_新增量'].map('{:,.0f}'.format)
df_new['治愈_新增量'] = df_new['治愈_新增量'].map('{:,.0f}'.format)


new_table = tabulate(
	df_new.loc[:,df_new.columns != 'Source'],
	headers = ['日期', '接触', '观察', '疑似', '确诊', '重症', '死亡', '治愈'],
	showindex = 'always',
	tablefmt = 'pipe',
	stralign = 'right'
)

# print(ltd_table)


df_change = df[[
	'日期', '接触_新增率', '观察_新增率', '疑似_新增率', '确诊_新增率', '重症_新增率', '死亡_新增率', '治愈_新增率', 'Source'
	]].iloc[::-1]

df_change['日期'] = df_change['日期'].map('{:%m/%d}'.format)
df_change['日期'] = df_change[['日期','Source']].apply(lambda row: "<a href='%s'>%s</a>" % (row['Source'], row['日期']), axis=1)
df_change['接触_新增率'] = df_change['接触_新增率'].map('{:,.1%}'.format)
df_change['观察_新增率'] = df_change['观察_新增率'].map('{:,.1%}'.format)
df_change['疑似_新增率'] = df_change['疑似_新增率'].map('{:,.1%}'.format)
df_change['确诊_新增率'] = df_change['确诊_新增率'].map('{:,.1%}'.format)
df_change['重症_新增率'] = df_change['重症_新增率'].map('{:,.1%}'.format)
df_change['死亡_新增率'] = df_change['死亡_新增率'].map('{:,.1%}'.format)
df_change['治愈_新增率'] = df_change['治愈_新增率'].map('{:,.1%}'.format)


change_table = tabulate(
	df_change.loc[:,df_change.columns != 'Source'],
	headers = ['日期', '接触', '观察', '疑似', '确诊', '重症', '死亡', '治愈'],
	showindex = 'always',
	tablefmt = 'pipe',
	stralign = 'right'
)

# print(change_table)

# construct the text portion of the README.md file

read_me_text = """
# 2020年新型冠状病毒感染趋势图

## 说明

这是根据卫建委发布的官方数据制作的每日疫情发展趋势图。每日830~930之间根据卫建委发布的最新疫情通报更新。

- 更新时间: **`08:30, %s`**
- [网页地址](https://zire.github.io/pandemic2020/)
- [Github Repo地址](https://github.com/zire/pandemic2020)
- 数据来源：[中华人民共和国国家卫生健康委员会卫生应急办公室](http://www.nhc.gov.cn/)
- 数据范围: 全中国
- 数据统计窗口：每日00 - 24小时
- 死亡率 = 当日累计死亡人数/当日累计确诊人数

## 疫情趋势图

疑似，确诊，重症，死亡，治愈 - 历史累计

![chart](charts/chart_big_5_ltd.png)

疑似，确诊 - 每日新增

![chart](charts/chart_big_2_net_new.png)

死亡，治愈 - 每日新增

![chart](charts/chart_DnC_net_new.png)

## 统计数据

### 累计

%s

### 当日新增

%s

### 当日新增百分比

%s

## 疫情蔓延时应该看什么电影

1. [Contagion (2011), IMDB 6.6, Matt Damon, Jude Law, Kate Winslet, Gwyneth Paltrow](https://www.imdb.com/title/tt1598778/). 这是跟目前的outbreak最接近的电影，几乎一模一样的情节。不要轻易跟厨师握手。
2. [World War Z (2013), IMDB 7.0, Brad Pitt](https://www.imdb.com/title/tt0816711/). 找到疫情源头至关重要，哪怕牺牲再多的海军陆战队员也再所不惜。身上有点小病未必是坏事。
3. [Outbreak (1995), IMDB 6.6, Dustin Hoffman, Rene Susso, Morgan Freeman, Kevin Bacon](https://www.imdb.com/title/tt0114069/). 论病毒的产生跟政府研究生化武器之间的关系。找到原始带菌者（电影里是一只猴子）是培育疫苗的关键。
4. [Train to Busan (2016), IMDB 7.5, Yoo Gong, Ma Dong-seok](https://www.imdb.com/title/tt5700672/). 在人群密集的地方如何保护自己，除了傍上马东锡这样的猛男以外
5. [Zombieland (2009), IMDB 7.6, Emma Stone, Woody Harrelson, Jesse Eisenberg](https://www.imdb.com/title/tt1156398/). 在非常时期里非常实用的求生手册
6. [Zombieland: Double Tap (2019), IMDB 6.8, Woody Harrelson, Jesse Eisenberg, Emma Stone](https://www.imdb.com/title/tt1560220/).在逃难时，四个人是比较合适的MDU (Minimum Deployment Unit）
7. [The Mist (2007), IMDB 7.1, Thomas Jane](https://www.imdb.com/title/tt0884328/). 是待在原地还是外冲？
8. [28 Days Later (2002), IMDB 7.6, Cillian Murphy, Naomie Harris](https://www.imdb.com/title/tt0289043/). 瘟疫横行时，人比病毒更让人恐惧
9. [Perfect Sense (2011), IMDB 7.1, Ewan McGregor, Eva Green](https://www.imdb.com/title/tt1439572/). 现在拥有的各种美好，不是理所当然的。
10. [War of the Worlds (2005), IMDB 6.5, Tom Cruise, Tim Robbins](https://www.imdb.com/title/tt0407304/). 如何开车逃生，以及避开人群的重要性
11. [Shaun of the Dead (2004), Simon Pegg, Nick Frost](https://www.imdb.com/title/tt0365748/). 不管在何种危难关头，都不能抛弃Prince的黑胶, Batman Forever的则可以。
12. [I Am Legend (2007), IMDB 7.2, Will Smith](https://www.imdb.com/title/tt0480249/). 
13. [Twelven Monkeys (1995), IMDB 8.0, Bruce Willis, Brad Pitt, Madeleine Stowe](https://www.imdb.com/title/tt0114746/). 
14. [Children of Men (2006), IMDB 7.9, Clive Owen, Julianne Moore, Chiwetel Ejiofor](https://www.imdb.com/title/tt0206634/).


"""

# Create complete README.md with variables

read_me_all = read_me_text % (current_date.strftime('%m-%d'), ltd_table, new_table, change_table)

md_file = "../README.md"

with open(md_file, 'w') as f:
	f.write(read_me_all)
	print("README.md updated!")





