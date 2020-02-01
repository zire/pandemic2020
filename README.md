# 2020年新型冠状病毒感染趋势图

## 说明

这是根据卫建委发布的官方数据制作的每日疫情发展趋势图。每日830~930之间根据卫建委发布的最新疫情通报更新。

- 更新时间: **`10:00, 2/1/2020`**
- [网页地址](https://zire.github.io/pandemic2020/)
- [Github Repo地址](https://github.com/zire/pandemic2020)
- 数据来源：[中华人民共和国国家卫生健康委员会卫生应急办公室](http://www.nhc.gov.cn/)
- 数据范围: 全中国
- 数据统计窗口：每日00 - 24小时
- 死亡率 = 当日死亡人数/当日确诊人数

## 疫情趋势图

历史累计

![chart](charts/pandemic_chart_YTD_all.png)

每日新增

![chart](charts/pandemic_chart_Net_New_all.png)

历史累计 - 死亡和治愈

![chart](charts/pandemic_chart_LTD_DnC.png)

## 统计数据

### 累计

| 日期 | 密切接触 | 接受医学观察 | 疑似病例 | 确诊 | 重症病例 | 死亡 | 治愈|
| --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
|1/31/2020|136,987|118,478|17,988|11,791|1,795|259|243|
|1/30/2020|113,579|102,427|15,238|9,692|1,527|213|171|
|1/29/2020|88,693|81,947|12,167|7,711|1,370|170|124|
|1/28/2020|65,537|59,990|9,239|5,974|1,239|132|103|
|1/27/2020|47,833|44,132|6,973|4,515|976|106|60|
|1/26/2020|32,799|30,453|5,794|2,744|461|80|51|
|1/25/2020 | 23,431 | 21,556| 2,684|1,975| 324|56|49|
|1/24/2020|15,197|13,967|1,965|1,287|237|41|38|
|1/23/2020|9,507|8,420|1,072|830|177|25|34|
|1/22/2020|5,897|4,928|393|571|95|17|N.A.|
|1/21/2020|2,197| 1,394| N.A. |440|102|9|N.A.|
|1/20/2020|1,739|922|54|291|N.A.|N.A.|N.A.|

### 当日新增百分比

| 日期 | 密切接触 | 接受医学观察 | 疑似病例 | 确诊 | 重症病例 | 死亡 | 治愈 |死亡率|
| --- | ---: | ---: | ---: | ---: | ---: | ---: | ---:| ---: |
|1/31/2020|21%|16%|18%|22%|18%|22%|42%|2.20%|
|1/30/2020|28%|25%|25%|26%|11%|25%|38%|2.20%|
|1/29/2020|35%|37%|32%|29%|11%|29%|20%|2.20%|
|1/28/2020|37%|36%|32%|32%|27%|25%|72%|2.21%|
|1/27/2020|46%|45%|20%|65%|112%|33%|18%|2.35%|
|1/26/2020|40%|41%|116%|39%|42%|43%|4%|2.92%|
|1/25/2020|54%|54%|37%|53%|37%|37%|29%|2.84%|
|1/24/2020|60%|66%|83%|55%|34%|64%|12%|3.19%|
|1/23/2020|61%|71%|173%|45%|86%|47%|N.A.|3.01%|
|1/22/2020|168%|254%|N.A.|30%|-7%|89%|N.A.|2.98%|
|1/21/2020|26%| 51%| N.A. |N.A.|N.A.|N.A.|N.A.|N.A.|

## 测算 

本测算模型非常简单，就是以目前的数字为原点，按照过去三天当日增长率的平均值来推算未来7天，14天，21天，28天的累计数字。譬如，第六天的数字为, 今日数字 x (1+平均日增长率)^6。考虑到整个模型对日增长率的敏感度，另外几个增长率的情景也做了测算，把日增长率往上下浮动10%和20%，大家可以凭自己心情和判断选择心仪的情景。这个模型唯一的原始参数就是目前的数字和日增长率，不对所谓的“拐点”做任何判断。

###  确诊数量

- Latest date as BOP (Beginning of Period): *`1/31/2020`*
- Latest average day-over-day % of the last 3 trailing days: *`25.5%`*
- Current life-to-date confirmed infected: *`11,791`*

| # of Days from 1/31 | -20% Adj | -10% Adj | 0% Adj | 10% Adj | 20% Adj |
| ---: |---: |---: |---: |---: |---:|
| | 20.4% |22.9%| 25.5%| 28.0%| 30.6%|
|7 | 43,194| 50,013|57,735|66,457|76,285|
|14|158,231|212,137|282,702|374,571|493,551| 
|21|579,647|899,808|1,384,261|2,111,186|3,193,178| 
|28|2,123,413|3,816,652|6,778,089|11,899,221|20,659,222|

### 死亡数量

- Latest date as BOP (Beginning of Period): *`1/31/2020`*
- Latest average day-over-day % of the last 3 trailing days: *`25.2%`*
- Current life-to-date deaths: *`259`*

| # of Days from 1/31 | -20% Adj | -10% Adj | 0% Adj | 10% Adj | 20% Adj |
| ---: |---: |---: |---: |---: |---:|
|7|	 938| 	 1,085| 	 1,251| 	 1,438| 	 1,649| 
|14|	 3,396|4,543 	 |6,040 	 |7,985| 	 10,500 
|21|	 12,298| 	 19,024| 	 29,167| 	 44,339| 66,853| 
|28|	 44,534| 	 79,669| 	 140,849| 	 246,196| 425,661| 

### 历史对比

|病毒|发现年|确诊病例|死亡数量|死亡率|感染国家|
|---|---|---:|---:|---:|---:|
|Marberg|1967|466|373|80%|11|
|Ebola|1976|33,577|13,562|40.4%|9|
|H5N1 Bird Flu|1997|861|455|52.80%|18|
|Nipah|1998|513|398|77.60%|2|
|SARS|2002|8,096|774|9.60%|29|
|H1N1|2009|1,632,258|284,500|17.40%|214|
|MERS|2012|2,494|858|34.40%|28|
|H7N9 Bird Flu|2013|1,568|616|39.30%|3|
|Wuhan|2020| 11,791|259|2.20%|N.A.|

Source:
- [Business Insider](https://www.businessinsider.com/wuhan-coronavirus-cases-total-sars-pandemic-cases-2020-1?r=US&IR=T)

## 疫情蔓延时应该看什么电影

1. [Contagion (2011), IMDB 6.6, Matt Damon, Jude Law, Kate Winslet, Gwyneth Paltrow](https://www.imdb.com/title/tt1598778/). 这是跟目前的outbreak最接近的电影，几乎一模一样的情节。不要轻易跟厨师握手。
2. [World War Z (2013), IMDB 7.0, Brad Pitt](https://www.imdb.com/title/tt0816711/). 找到疫情源头至关重要，哪怕牺牲再多的海军陆战队员也再所不惜。身上有点小病未必是坏事。
3. [Outbreak (1995), IMDB 6.6, Dustin Hoffman, Rene Susso, Morgan Freeman, Kevin Bacon](https://www.imdb.com/title/tt0114069/). 论病毒的产生跟政府研究生化武器之间的关系。找到原始带菌者（电影里是一只猴子）是培育疫苗的关键。
4. [Train to Fushan (2016), IMDB 7.5, Yoo Gong, Ma Dong-seok](https://www.imdb.com/title/tt5700672/). 在人群密集的地方如何保护自己，除了傍上马东锡这样的猛男以外
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

- [截至1月31日24时新型冠状病毒感染的肺炎疫情最新情况](http://www.nhc.gov.cn/xcs/yqfkdt/202002/84faf71e096446fdb1ae44939ba5c528.shtml)
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