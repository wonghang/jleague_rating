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
丸安岡崎 => -0.217086
日聯U22 => -0.200225
岡山綠雉二隊 => -0.196062
橫濱SCC => -0.174213
櫪木葡萄 => -0.167665
富山勝利 => -0.160832
FC岐阜 => -0.154127
藤枝MYFC => -0.150017
流通經濟大學 => -0.140223
群馬草津溫泉 => -0.105138
盛岡仙鶴 => -0.100612
MIO草津琵琶湖 => -0.0991446
鳥取飛翔 => -0.087998
德島漩渦 => -0.0865933
水戶蜀葵 => -0.0821803
本田制鎖 => -0.0808891
FC愛媛 => -0.0806812
AC大分 => -0.0737704
熊本羅亞素 => -0.066808
大分三神 => -0.0601403
秋田藍閃電 => -0.0598763
福島聯 => -0.0566984
FC橫濱 => -0.0519775
FC琉球 => -0.0491037
讚岐卡馬達馬尼 => -0.0468371
岡山綠雉 => -0.0401763
北九州向日葵 => -0.0343775
橫河武藏野 => -0.0332359
山形山神 => -0.0326512
千葉市原青年隊 => -0.0304993
大宮松鼠 => -0.0286649
高崎藝術 => -0.0189551
福岡黃蜂 => -0.0175221
東京綠茵 => -0.017431
清水心跳 => -0.0154566
福岡大學 => -0.0149469
京都不死鳥 => -0.0141586
高知大學 => -0.0129942
福井恐龍 => -0.0117656
札幌岡薩多 => -0.011657
富山新莊 => -0.00985773
新潟天鵝 => -0.00873356
順天堂大學 => -0.00611973
日本足球學院 => -0.0058306
北陸大學 => -0.00577371
FC刈谷 => -0.00303816
三菱水島 => -0.00290823
奈良俱樂部 => -0.00272521
東京國際大學 => -0.00250237
明治大學 => -0.00175918
FC大阪 => -0.00161716
鹿屋體育大學 => -0.00124751
FC岐阜B隊 => -0.0011982
關西學院大學 => -0.00101515
圖南前橋 => 4.43168e-06
東海大學熊本 => 7.49454e-06
和歌山艾特里武 => 5.34936e-05
島根體育會 => 0.000191272
築波大學 => 0.000191272
沖繩 => 0.000191274
今治 => 0.000292183
佐賀大學 => 0.00109153
大阪體育大學 => 0.00109153
德島漩渦青年隊 => 0.00109153
關西大學 => 0.00109153
愛媛島並 => 0.00109153
桑名14 => 0.00109153
多度津 => 0.00196326
桐蔭橫濱大學 => 0.00198003
四日市大學 => 0.00198899
山形大學 => 0.00199144
三菱重工長崎 => 0.00199486
韭崎 => 0.0019986
廣島經濟大學 => 0.00199972
松江市FC => 0.0020015
立命館大學 => 0.0020842
NORD北海道 => 0.00208797
神戶山賊十一 => 0.00208797
埼玉SC => 0.00208797
佐賀東高校 => 0.00208797
維特菲高原 => 0.00208797
日本文理大學 => 0.00208797
熊本學園大學附屬高校 => 0.00208797
中京大學 => 0.00208797
駒澤大學 => 0.00208797
北海道大學 => 0.00208797
鈴鹿藍寶利 => 0.00208797
浦安SC => 0.00208797
豊田蹴球團 => 0.00208797
德山大學 => 0.00208797
潤梅爾青森 => 0.00344774
德島大學 => 0.00344774
佐賀LIXIL => 0.00344774
JFC宮崎 => 0.00344774
札幌大學 => 0.00344774
成蹊大學 => 0.00344792
FC靜岡 => 0.00344792
猿田興業 => 0.00344792
靜岡產業大學 => 0.00344792
FC水島 => 0.00344792
國士館大學 => 0.00344792
鳥取夢想 => 0.00344792
三重大學 => 0.00344792
浩運 => 0.00344792
青森山田高校 => 0.00344792
福山大學 => 0.00344792
熊本學園大學 => 0.00344792
巴拉費勒米澤 => 0.00344792
巴連特富山 => 0.00344792
尚美大學 => 0.00344792
濱田宇宙 => 0.00344792
佐川中國SC => 0.00344792
東京綠茵青年隊 => 0.00344792
玉穗FC => 0.00344792
米子北高校 => 0.00344792
環太平洋大學 => 0.00344792
福岡教育大學 => 0.00344792
艾美高斯鹿兒島 => 0.00344792
三洋電機洲本 => 0.00344792
宮崎產業經營大學 => 0.00344792
柏雷素爾U18 => 0.00344792
鹿兒島火山 => 0.00344792
高松商高校 => 0.00344792
新潟經營大學 => 0.00344792
琵琶湖成蹊體育大學 => 0.00344792
岐阜經濟大學 => 0.00344792
京都產業大學 => 0.00344792
山梨學院大學附屬高校 => 0.00344792
德島市立高中 => 0.00344792
SRC廣島 => 0.00344792
上田魂 => 0.00344792
熊本教員蹴友團 => 0.00344792
神戶勝利船 => 0.0104609
甲府風林 => 0.018178
湘南比馬 => 0.0251236
千葉市原 => 0.0287366
磐田山葉 => 0.0296735
長崎成功丸 => 0.0297321
松本山雅 => 0.0319914
SC相模原 => 0.0393495
仙台維加泰 => 0.0454915
佐川急便滋賀 => 0.0509258
大阪櫻花 => 0.0533919
金澤薩維根 => 0.0565782
鳥棲砂岩 => 0.0660711
佐川印刷 => 0.0705519
川崎前鋒 => 0.0787064
FC仙台 => 0.0839376
八戶雲羅里 => 0.0875501
沼津青藍 => 0.0916813
名古屋八鯨 => 0.0922489
柏雷素爾 => 0.0948848
橫濱水手 => 0.0971081
FC東京 => 0.108155
廣島三箭 => 0.118006
町田澤維亞 => 0.123341
浦和紅鑽 => 0.12816
FC本田 => 0.132533
鹿兒島聯 => 0.143419
大阪飛腳 => 0.150023
鹿島鹿角 => 0.150961
長野帕塞羅 => 0.183793
山口雷法 => 0.194005
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
