# jleague_rating
Japan J League Ratings computed from eigenvectors.

This code computes the ratings of Japan League football team from their raw data.

# The Algorithm

The code implements

Brent, Richard P. "Note on Computing Ratings from Eigenvectors." _arXiv preprint_ arXiv:[1005.0762](https://arxiv.org/abs/1005.0762) (2010).

The problem is as follow:

There are <img alt="$n$" src="svgs/55a049b8f161ae7cfeb0197d75aff967.png" align="middle" width="9.867000000000003pt" height="14.155350000000013pt"/> players playing among each other in a zero-sum game for several times. Assume a WIN score 1 mark, a DRAW score 0.5 marks and a LOSE scores 0 marks. We obtain a score matrix <img alt="$S = (s_{ij})$" src="svgs/00f350d27b8e3b502310f0ace7ce89b1.png" align="middle" width="65.0133pt" height="24.65759999999998pt"/>.

We want to compute a rating <img alt="$r_i$" src="svgs/3cf87ea38a615ed99e0232f8ed9431fe.png" align="middle" width="12.067275000000004pt" height="14.155350000000013pt"/> for each player <img alt="$i$" src="svgs/77a3b857d53fb44e33b53e4c8b68351a.png" align="middle" width="5.663295000000005pt" height="21.683310000000006pt"/> from the score matrix <img alt="$S$" src="svgs/e257acd1ccbe7fcb654708f1a866bfe9.png" align="middle" width="11.027445000000004pt" height="22.46574pt"/>. The ratings should capture the relative strength of the players.

We assume the rating <img alt="$r_i$" src="svgs/3cf87ea38a615ed99e0232f8ed9431fe.png" align="middle" width="12.067275000000004pt" height="14.155350000000013pt"/> and <img alt="$r_j$" src="svgs/212f899c5235a861a1f6146dc8d1582f.png" align="middle" width="13.520925000000005pt" height="14.155350000000013pt"/> will compute the expected score of a player <img alt="$i$" src="svgs/77a3b857d53fb44e33b53e4c8b68351a.png" align="middle" width="5.663295000000005pt" height="21.683310000000006pt"/> in a game against player <img alt="$j$" src="svgs/36b5afebdba34564d884d347484ac0c7.png" align="middle" width="7.710483000000004pt" height="21.683310000000006pt"/> as <img alt="$f(r_i - r_j)$" src="svgs/3b03c5390eb15e78ef471bd6b3254bcc.png" align="middle" width="69.92601pt" height="24.65759999999998pt"/> for some function <img alt="$f: \mathbb{R} \to [0,1]$" src="svgs/eee6982d58163a355d800d004a5530fc.png" align="middle" width="93.8355pt" height="24.65759999999998pt"/>.

Under some reasonable assumptions, we assume <img alt="$f$" src="svgs/190083ef7a1625fbc75f243cffb9c96d.png" align="middle" width="9.817500000000004pt" height="22.831379999999992pt"/> is a logistic function:

<p align="center"><img alt="$$&#10;f(z) = \frac{1}{1+e^{-cz}}&#10;$$" src="svgs/49fd20390266bb6d3fb0984d0fcba84d.png" align="middle" width="114.548115pt" height="34.360095pt"/></p>

for some number <img alt="$c$" src="svgs/3e18a4a28fdee1744e5e3f79d13b9ff6.png" align="middle" width="7.113876000000004pt" height="14.155350000000013pt"/>. In this implementation, <img alt="$c=1$" src="svgs/2a24f4b966bec8b31d29ed41eb258910.png" align="middle" width="37.250730000000004pt" height="21.18732pt"/>.

Under this assumption, the solution to the problem can be reduced into a linear eigenvalue problem.

The code implements an efficient sparse and online version of the algorithm (i.e., new data can be fed into the algorithm to update previously computed ratings).

The code adds a dummy player who makes a DRAW game with all the other players to resolve the potential degenerate issue.  (See the paper for details)

The dummy player has the name "" (empty string) and must have index 0.

# Dependencies

The code depends on [numpy](https://numpy.org/), [pandas](https://pandas.pydata.org/) and [matplotlib](https://matplotlib.org/).

# Example


```shell
> python3 jleague_rating.py
丸安岡崎 => -0.216217
日聯U22 => -0.198914
岡山綠雉二隊 => -0.195038
橫濱SCC => -0.17138
櫪木葡萄 => -0.156585
富山勝利 => -0.152091
藤枝MYFC => -0.147124
FC岐阜 => -0.144217
流通經濟大學 => -0.137584
盛岡仙鶴 => -0.0993401
MIO草津琵琶湖 => -0.0939883
群馬草津溫泉 => -0.08984
鳥取飛翔 => -0.0808774
本田制鎖 => -0.0756055
德島漩渦 => -0.0713801
AC大分 => -0.0709794
FC愛媛 => -0.0673518
水戶蜀葵 => -0.0670971
熊本羅亞素 => -0.056303
福島聯 => -0.0543888
秋田藍閃電 => -0.0542096
大分三神 => -0.0462374
FC琉球 => -0.0436989
讚岐卡馬達馬尼 => -0.0414955
FC橫濱 => -0.0375992
岡山綠雉 => -0.031094
橫河武藏野 => -0.0280764
千葉市原青年隊 => -0.0272397
北九州向日葵 => -0.0258384
福岡大學 => -0.0175484
山形山神 => -0.0173623
高知大學 => -0.0157313
高崎藝術 => -0.0156999
大宮松鼠 => -0.014537
福井恐龍 => -0.0144919
富山新莊 => -0.0126715
順天堂大學 => -0.00879611
日本足球學院 => -0.00866162
北陸大學 => -0.00860674
東京國際大學 => -0.00536087
明治大學 => -0.00448941
鹿屋體育大學 => -0.00404748
FC岐阜B隊 => -0.00402275
關西學院大學 => -0.00383583
福岡黃蜂 => -0.00341503
圖南前橋 => -0.0028931
東海大學熊本 => -0.00289011
FC刈谷 => -0.00283369
和歌山艾特里武 => -0.00279476
島根體育會 => -0.00265975
築波大學 => -0.00265975
沖繩 => -0.00265974
今治 => -0.00255339
東京綠茵 => -0.0023729
三菱水島 => -0.00235745
奈良俱樂部 => -0.00229684
佐賀大學 => -0.00179309
大阪體育大學 => -0.00179309
德島漩渦青年隊 => -0.00179309
關西大學 => -0.00179309
愛媛島並 => -0.00179309
桑名14 => -0.00179309
FC大阪 => -0.00127489
多度津 => -0.00112802
桐蔭橫濱大學 => -0.00111029
四日市大學 => -0.00110173
山形大學 => -0.00109855
三菱重工長崎 => -0.00109538
韭崎 => -0.00109175
廣島經濟大學 => -0.00109127
松江市FC => -0.00108786
立命館大學 => -0.00100045
NORD北海道 => -0.000998306
神戶山賊十一 => -0.000998306
埼玉SC => -0.000998306
佐賀東高校 => -0.000998306
維特菲高原 => -0.000998306
日本文理大學 => -0.000998306
熊本學園大學附屬高校 => -0.000998306
中京大學 => -0.000998306
駒澤大學 => -0.000998306
北海道大學 => -0.000998306
鈴鹿藍寶利 => -0.000998306
浦安SC => -0.000998306
豊田蹴球團 => -0.000998306
德山大學 => -0.000998306
清水心跳 => -0.000733769
德島大學 => -0.000420364
潤梅爾青森 => -0.000420362
佐賀LIXIL => -0.000420359
JFC宮崎 => -0.000420357
札幌大學 => -0.000420355
成蹊大學 => -0.000420155
FC靜岡 => -0.000420155
猿田興業 => -0.000420155
靜岡產業大學 => -0.000420155
FC水島 => -0.000420155
國士館大學 => -0.000420155
鳥取夢想 => -0.000420155
三重大學 => -0.000420155
浩運 => -0.000420155
青森山田高校 => -0.000420155
福山大學 => -0.000420155
熊本學園大學 => -0.000420155
巴拉費勒米澤 => -0.000420155
巴連特富山 => -0.000420155
尚美大學 => -0.000420155
濱田宇宙 => -0.000420155
佐川中國SC => -0.000420155
東京綠茵青年隊 => -0.000420155
玉穗FC => -0.000420155
米子北高校 => -0.000420155
環太平洋大學 => -0.000420155
福岡教育大學 => -0.000420155
艾美高斯鹿兒島 => -0.000420155
三洋電機洲本 => -0.000420155
宮崎產業經營大學 => -0.000420155
柏雷素爾U18 => -0.000420155
鹿兒島火山 => -0.000420155
高松商高校 => -0.000420155
新潟經營大學 => -0.000420155
琵琶湖成蹊體育大學 => -0.000420155
岐阜經濟大學 => -0.000420155
京都產業大學 => -0.000420155
山梨學院大學附屬高校 => -0.000420155
德島市立高中 => -0.000420155
SRC廣島 => -0.000420155
上田魂 => -0.000420155
熊本教員蹴友團 => -0.000420155
京都不死鳥 => 8.70993e-05
札幌岡薩多 => 0.00136048
新潟天鵝 => 0.00378042
神戶勝利船 => 0.0250624
甲府風林 => 0.0332921
長崎成功丸 => 0.0370285
松本山雅 => 0.0392064
湘南比馬 => 0.0400538
SC相模原 => 0.0414345
千葉市原 => 0.0429511
磐田山葉 => 0.0438624
佐川急便滋賀 => 0.0558644
仙台維加泰 => 0.0613286
金澤薩維根 => 0.0618061
大阪櫻花 => 0.067829
佐川印刷 => 0.0758816
鳥棲砂岩 => 0.0816959
八戶雲羅里 => 0.0886972
FC仙台 => 0.0891531
沼津青藍 => 0.0925661
川崎前鋒 => 0.0930826
名古屋八鯨 => 0.106527
柏雷素爾 => 0.109249
橫濱水手 => 0.112469
FC東京 => 0.122261
町田澤維亞 => 0.129119
廣島三箭 => 0.132041
FC本田 => 0.13815
浦和紅鑽 => 0.142672
鹿兒島聯 => 0.144378
大阪飛腳 => 0.162988
鹿島鹿角 => 0.165443
長野帕塞羅 => 0.187487
山口雷法 => 0.19531
```

The bigger the rating is, the stronger the team is.
As the code implements an online algorithm, one can plot the ratings of teams against the dates:
(The first 100 data points are not plotted)

```shell
> python3 jleague_rating.py 鹿島鹿角 浦和紅鑽 清水心跳
```

![Figure_1.png](Figure_1.png?raw=true "Figure 1")

# Data

The data is stored in `japan_soccer.csv`. It consists of all Japan League football matches from 2005 Jan 1 to 2015 Dec 31. The data was collected from various sources by me.

The meaning of the field:

| field | meaning |
| --- | --- |
| date | Date of the football match |
| league | League of the match (see below) |
| home | Name of home team |
| away | Name of away team |
| neutral | 1 indicates the venue is neutral. 0 if not |
| full-home | Home team's number of goals (full match) |
| full-away | Away team's number of goals (full match) |
| half-home | Home team's number of goals (half match) |
| half-away | Away team's number of goals (half match) |
| corner-home | Home team's number of corners |
| corner-away | Away team's number of corners |
| redcard-home | Home team's number of red cards |
| redcard-away | Away team's number of red cards |

| league | League Name |
| --- | --- |
| JD1 | J1 League |
| JD2 | J2 League |
| JD3 | J3 League |
| JDP | Extra matches in J. League |
| JEC | The Emperor's Cup (サッカー天皇杯) |
| JFL | Japan Football League (for amateur) |
| JLC | J. League Cup |
| JSC | Japan Super Cup (富士ゼロックス スーパーカップ) |
| 1JSTL | Japan Satellite League |

Any -1 in the data means missing data.

# API

To use `online_brent_rating`, creating an object:

```python
>>> from brent_rating import *
>>> br = online_brent_rating()
```

Before you add any new match data to it, you need to create the names first.

```python
>>> br.new_name("A")
1
>>> br.new_name("B")
2
>>> br.new_name("C")
3
>>> 
```

To feed matchs' results, please do the followings:

```python
>>> br.start()
>>> br.add("A","B",1) # A vs B => A wins
>>> br.add("B","C",1) # B vs C => B wins
>>> br.add("C","A",-1) # C vs A => C loses
>>> br.add("B","C",0) # B vs C => draw game
>>> br.commit()
```

You may specify a decay term by `br.commit(decay=0.99)` so that old matches have fewer weights.

You can get the ratings by `br.current()`

```python
>>> br.current()
array([ 0.        ,  1.26869486, -0.21202082, -0.98304483])
```

or 

```python
>>> br.get("A")
1.2686948633315682
>>> br["A"]
1.2686948633315682
```

Any non-exist name returns 0.

```python
>>> br["ABC"]
0.0
```

iterator interface is available:

```python
>>> for (name,rating) in br:
...   print(name,rating)
... 
A 1.2686948633315682
B -0.2120208244815574
C -0.9830448286353088
>>> 
```

A simple `predict` function to compute the expected score is available as well:

```python
>>> br.predict("A","B")
0.8146806567861219
>>> br.predict("B","C")
0.6837423647588244
>>> br.predict("C","B")
0.3162576352411756
>>> 
```
