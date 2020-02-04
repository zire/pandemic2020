import numpy as np 
import pandas as pd 
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
from tabulate import tabulate

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
	y=['疑似_新增量', '确诊_新增量', '重症_新增量','死亡_新增量'],
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

# ----------- Create README.md ------------------------------------------------

current_date = df['日期'].iat[-1]

df_ltd = df[['日期', '接触', '观察', '疑似', '确诊', '重症', '死亡', '治愈']].iloc[::-1]

# print(df_ltd['日期'])

# df_ltd['日期'] = pd.to_datetime(df_ltd['日期'], format="%m/%d")

# print(df_ltd['日期'].strftime('%m/%d'))

df_ltd['日期'] = df_ltd['日期'].map('{:%m/%d}'.format)
df_ltd['接触'] = df_ltd['接触'].map('{:,.0f}'.format)
df_ltd['观察'] = df_ltd['观察'].map('{:,.0f}'.format)
df_ltd['疑似'] = df_ltd['疑似'].map('{:,.0f}'.format)
df_ltd['确诊'] = df_ltd['确诊'].map('{:,.0f}'.format)
df_ltd['重症'] = df_ltd['重症'].map('{:,.0f}'.format)
df_ltd['死亡'] = df_ltd['死亡'].map('{:,.0f}'.format)
df_ltd['治愈'] = df_ltd['治愈'].map('{:,.0f}'.format)

ltd_table = tabulate(
	df_ltd,
	headers = ['日期', '接触', '观察', '疑似', '确诊', '重症', '死亡', '治愈'],
	showindex = 'always',
	tablefmt = 'pipe',
	stralign = 'right'
)

# print(ltd_table)

df_change = df[[
	'日期', '接触_新增率', '观察_新增率', '疑似_新增率', '确诊_新增率', '重症_新增率', '死亡_新增率', '治愈_新增率'
	]].iloc[::-1]

df_change['日期'] = df_change['日期'].map('{:%m/%d}'.format)
df_change['接触_新增率'] = df_change['接触_新增率'].map('{:,.1%}'.format)
df_change['观察_新增率'] = df_change['观察_新增率'].map('{:,.1%}'.format)
df_change['疑似_新增率'] = df_change['疑似_新增率'].map('{:,.1%}'.format)
df_change['确诊_新增率'] = df_change['确诊_新增率'].map('{:,.1%}'.format)
df_change['重症_新增率'] = df_change['重症_新增率'].map('{:,.1%}'.format)
df_change['死亡_新增率'] = df_change['死亡_新增率'].map('{:,.1%}'.format)
df_change['治愈_新增率'] = df_change['治愈_新增率'].map('{:,.1%}'.format)


change_table = tabulate(
	df_change,
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

历史累计

![chart](charts/chart_big_4_ltd.png)

每日新增

![chart](charts/chart_big_4_net_new.png)

历史累计 - 死亡和治愈

![chart](charts/chart_DnC_LTD.png)

## 统计数据

### 累计

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

## 数据来源

- [截至2月2日24时新型冠状病毒感染的肺炎疫情最新情况](http://www.nhc.gov.cn/xcs/yqfkdt/202002/24a796819bf747bd8b945384517e9a51.shtml)
- [截至2月1日24时新型冠状病毒感染的肺炎疫情最新情况](http://www.nhc.gov.cn/xcs/yqtb/202002/d5c495da742f4739b7f99339c3bd032f.shtml)
- [截至1月31日24时新型冠状病毒感染的肺炎疫情最新情况](http://www.nhc.gov.cn/xcs/yqtb/202002/84faf71e096446fdb1ae44939ba5c528.shtml)
- [截至1月30日24时新型冠状病毒感染的肺炎疫情最新情况](http://www.nhc.gov.cn/xcs/yqtb/202001/a53e6df293cc4ff0b5a16ddf7b6b2b31.shtml)
- [截至1月29日24时新型冠状病毒感染的肺炎疫情最新情况](http://www.nhc.gov.cn/xcs/yqtb/202001/e71bd2e7a0824ca69f87bbf1bef2a3c9.shtml)
- [截至1月28日24时新型冠状病毒感染的肺炎疫情最新情况](http://www.nhc.gov.cn/xcs/yqtb/202001/1c259a68d81d40abb939a0781c1fe237.shtml)
- [截至1月27日24时新型冠状病毒感染的肺炎疫情最新情况](http://www.nhc.gov.cn/xcs/yqtb/202001/ec9fe7ea987d467d9462e7db509079e6.shtml)
- [截至1月26日24时新型冠状病毒感染的肺炎疫情最新情况](http://www.nhc.gov.cn/xcs/yqtb/202001/3882fdcdbfdc4b4fa4e3a829b62d518e.shtml)
- [截至1月25日24时新型冠状病毒感染的肺炎疫情最新情况](http://www.nhc.gov.cn/xcs/yqtb/202001/9614b05a8cac4ffabac10c4502fe517c.shtml)
- [截至1月24日24时新型冠状病毒感染的肺炎疫情最新情况](http://www.nhc.gov.cn/xcs/yqtb/202001/a7cf0437d1324aed9cc1b890b8ee29e6.shtml)
- [1月23日新型冠状病毒感染的肺炎疫情情况](http://www.nhc.gov.cn/xcs/yqtb/202001/5d19a4f6d3154b9fae328918ed2e3c8a.shtml)
- [1月22日新型冠状病毒感染的肺炎疫情情况](http://www.nhc.gov.cn/xcs/yqtb/202001/a3c8b5144067417889d8760254b1a7ca.shtml)
- [1月21日新型冠状病毒感染的肺炎疫情情况](http://www.nhc.gov.cn/xcs/yqtb/202001/930c021cdd1f46dc832fc27e0cc465c8.shtml)
"""

# Create complete README.md with variables

read_me_all = read_me_text % (current_date.strftime('%m-%d'), ltd_table, change_table)

md_file = "../README.md"

with open(md_file, 'w') as f:
	f.write(read_me_all)
	print("README.md updated!")





