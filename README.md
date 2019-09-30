# jleague_rating
Japan J League Ratings computed from eigenvectors

This code computes the ratings of Japan League football team from their raw data.

# The Algorithm

The code implements

> Brent, Richard P. "Note on Computing Ratings from Eigenvectors." * *arXiv preprint* * arXiv:[1005.0762](https://arxiv.org/abs/1005.0762) (2010).

The problem is as follow:

There are <img alt="$n$" src="svgs/55a049b8f161ae7cfeb0197d75aff967.png" align="middle" width="9.867000000000003pt" height="14.155350000000013pt"/> players playing among each other in a zero-sum game for several times. Assume a WIN score 1 mark, a DRAW score 0.5 marks and a LOSE scores 0 marks. We obtained a score matrix <img alt="$s_{ij}$" src="svgs/8184020a45b4be8100982ccf94eb83a1.png" align="middle" width="18.461025pt" height="14.155350000000013pt"/>.

We want to compute a rating <img alt="$r_i$" src="svgs/3cf87ea38a615ed99e0232f8ed9431fe.png" align="middle" width="12.067275000000004pt" height="14.155350000000013pt"/> for each player <img alt="$i$" src="svgs/77a3b857d53fb44e33b53e4c8b68351a.png" align="middle" width="5.663295000000005pt" height="21.683310000000006pt"/> from the score matrix <img alt="$S = (s_{ij})$" src="svgs/00f350d27b8e3b502310f0ace7ce89b1.png" align="middle" width="65.0133pt" height="24.65759999999998pt"/>. The ratings should capture the relative strength of the players.

To start with, we assume the rating <img alt="$r_i$" src="svgs/3cf87ea38a615ed99e0232f8ed9431fe.png" align="middle" width="12.067275000000004pt" height="14.155350000000013pt"/> and <img alt="$r_j$" src="svgs/212f899c5235a861a1f6146dc8d1582f.png" align="middle" width="13.520925000000005pt" height="14.155350000000013pt"/> would capture the expected score of a player <img alt="$i$" src="svgs/77a3b857d53fb44e33b53e4c8b68351a.png" align="middle" width="5.663295000000005pt" height="21.683310000000006pt"/> in a game against player <img alt="$j$" src="svgs/36b5afebdba34564d884d347484ac0c7.png" align="middle" width="7.710483000000004pt" height="21.683310000000006pt"/> as <img alt="$f(r_i - r_j)$" src="svgs/3b03c5390eb15e78ef471bd6b3254bcc.png" align="middle" width="69.92601pt" height="24.65759999999998pt"/> for some function <img alt="$f: \mathbb{R} \to [0,1]$" src="svgs/eee6982d58163a355d800d004a5530fc.png" align="middle" width="93.8355pt" height="24.65759999999998pt"/>.

Under some reasonable assumptions, we assume <img alt="$f$" src="svgs/190083ef7a1625fbc75f243cffb9c96d.png" align="middle" width="9.817500000000004pt" height="22.831379999999992pt"/> is a logistic function:

<p align="center"><img alt="$$&#10;f(z) = \frac{1}{1+e^{-cz}}&#10;$$" src="svgs/49fd20390266bb6d3fb0984d0fcba84d.png" align="middle" width="114.548115pt" height="34.360095pt"/></p>

for some number <img alt="$c$" src="svgs/3e18a4a28fdee1744e5e3f79d13b9ff6.png" align="middle" width="7.113876000000004pt" height="14.155350000000013pt"/>.

Under this assumption, the solution to the problem reduces into an eigenvalue problem. The code computes the solution by power method.

The code implements an efficient sparse and online version of the algorithm (i.e., new data can be fed into the algorithm to update previously computed ratings).
The code adds a dummy player who makes a DRAW game with all the other players to resolve the potential degenerate issue.  (See the paper for details)
The dummy player has the name "" (empty string) and must have index 0.

# Dependencies

The code requires [numpy](https://numpy.org/), [pandas](https://pandas.pydata.org/) and [matplotlib](https://matplotlib.org/).

# Example


```shell
<img alt="$ python3 jleague_rating.py&#10;丸安岡崎 =&gt; -0.217086&#10;日聯U22 =&gt; -0.200225&#10;岡山綠雉二隊 =&gt; -0.196062&#10;橫濱SCC =&gt; -0.174213&#10;櫪木葡萄 =&gt; -0.167665&#10;富山勝利 =&gt; -0.160832&#10;FC岐阜 =&gt; -0.154127&#10;藤枝MYFC =&gt; -0.150017&#10;流通經濟大學 =&gt; -0.140223&#10;群馬草津溫泉 =&gt; -0.105138&#10;盛岡仙鶴 =&gt; -0.100612&#10;MIO草津琵琶湖 =&gt; -0.0991446&#10;鳥取飛翔 =&gt; -0.087998&#10;德島漩渦 =&gt; -0.0865933&#10;水戶蜀葵 =&gt; -0.0821803&#10;本田制鎖 =&gt; -0.0808891&#10;FC愛媛 =&gt; -0.0806812&#10;AC大分 =&gt; -0.0737704&#10;熊本羅亞素 =&gt; -0.066808&#10;大分三神 =&gt; -0.0601403&#10;秋田藍閃電 =&gt; -0.0598763&#10;福島聯 =&gt; -0.0566984&#10;FC橫濱 =&gt; -0.0519775&#10;FC琉球 =&gt; -0.0491037&#10;讚岐卡馬達馬尼 =&gt; -0.0468371&#10;岡山綠雉 =&gt; -0.0401763&#10;北九州向日葵 =&gt; -0.0343775&#10;橫河武藏野 =&gt; -0.0332359&#10;山形山神 =&gt; -0.0326512&#10;千葉市原青年隊 =&gt; -0.0304993&#10;大宮松鼠 =&gt; -0.0286649&#10;高崎藝術 =&gt; -0.0189551&#10;福岡黃蜂 =&gt; -0.0175221&#10;東京綠茵 =&gt; -0.017431&#10;清水心跳 =&gt; -0.0154566&#10;福岡大學 =&gt; -0.0149469&#10;京都不死鳥 =&gt; -0.0141586&#10;高知大學 =&gt; -0.0129942&#10;福井恐龍 =&gt; -0.0117656&#10;札幌岡薩多 =&gt; -0.011657&#10;富山新莊 =&gt; -0.00985773&#10;新潟天鵝 =&gt; -0.00873356&#10;順天堂大學 =&gt; -0.00611973&#10;日本足球學院 =&gt; -0.0058306&#10;北陸大學 =&gt; -0.00577371&#10;FC刈谷 =&gt; -0.00303816&#10;三菱水島 =&gt; -0.00290823&#10;奈良俱樂部 =&gt; -0.00272521&#10;東京國際大學 =&gt; -0.00250237&#10;明治大學 =&gt; -0.00175918&#10;FC大阪 =&gt; -0.00161716&#10;鹿屋體育大學 =&gt; -0.00124751&#10;FC岐阜B隊 =&gt; -0.0011982&#10;關西學院大學 =&gt; -0.00101515&#10;圖南前橋 =&gt; 4.43168e-06&#10;東海大學熊本 =&gt; 7.49454e-06&#10;和歌山艾特里武 =&gt; 5.34936e-05&#10;島根體育會 =&gt; 0.000191272&#10;築波大學 =&gt; 0.000191272&#10;沖繩 =&gt; 0.000191274&#10;今治 =&gt; 0.000292183&#10;佐賀大學 =&gt; 0.00109153&#10;大阪體育大學 =&gt; 0.00109153&#10;德島漩渦青年隊 =&gt; 0.00109153&#10;關西大學 =&gt; 0.00109153&#10;愛媛島並 =&gt; 0.00109153&#10;桑名14 =&gt; 0.00109153&#10;多度津 =&gt; 0.00196326&#10;桐蔭橫濱大學 =&gt; 0.00198003&#10;四日市大學 =&gt; 0.00198899&#10;山形大學 =&gt; 0.00199144&#10;三菱重工長崎 =&gt; 0.00199486&#10;韭崎 =&gt; 0.0019986&#10;廣島經濟大學 =&gt; 0.00199972&#10;松江市FC =&gt; 0.0020015&#10;立命館大學 =&gt; 0.0020842&#10;NORD北海道 =&gt; 0.00208797&#10;神戶山賊十一 =&gt; 0.00208797&#10;埼玉SC =&gt; 0.00208797&#10;佐賀東高校 =&gt; 0.00208797&#10;維特菲高原 =&gt; 0.00208797&#10;日本文理大學 =&gt; 0.00208797&#10;熊本學園大學附屬高校 =&gt; 0.00208797&#10;中京大學 =&gt; 0.00208797&#10;駒澤大學 =&gt; 0.00208797&#10;北海道大學 =&gt; 0.00208797&#10;鈴鹿藍寶利 =&gt; 0.00208797&#10;浦安SC =&gt; 0.00208797&#10;豊田蹴球團 =&gt; 0.00208797&#10;德山大學 =&gt; 0.00208797&#10;潤梅爾青森 =&gt; 0.00344774&#10;德島大學 =&gt; 0.00344774&#10;佐賀LIXIL =&gt; 0.00344774&#10;JFC宮崎 =&gt; 0.00344774&#10;札幌大學 =&gt; 0.00344774&#10;成蹊大學 =&gt; 0.00344792&#10;FC靜岡 =&gt; 0.00344792&#10;猿田興業 =&gt; 0.00344792&#10;靜岡產業大學 =&gt; 0.00344792&#10;FC水島 =&gt; 0.00344792&#10;國士館大學 =&gt; 0.00344792&#10;鳥取夢想 =&gt; 0.00344792&#10;三重大學 =&gt; 0.00344792&#10;浩運 =&gt; 0.00344792&#10;青森山田高校 =&gt; 0.00344792&#10;福山大學 =&gt; 0.00344792&#10;熊本學園大學 =&gt; 0.00344792&#10;巴拉費勒米澤 =&gt; 0.00344792&#10;巴連特富山 =&gt; 0.00344792&#10;尚美大學 =&gt; 0.00344792&#10;濱田宇宙 =&gt; 0.00344792&#10;佐川中國SC =&gt; 0.00344792&#10;東京綠茵青年隊 =&gt; 0.00344792&#10;玉穗FC =&gt; 0.00344792&#10;米子北高校 =&gt; 0.00344792&#10;環太平洋大學 =&gt; 0.00344792&#10;福岡教育大學 =&gt; 0.00344792&#10;艾美高斯鹿兒島 =&gt; 0.00344792&#10;三洋電機洲本 =&gt; 0.00344792&#10;宮崎產業經營大學 =&gt; 0.00344792&#10;柏雷素爾U18 =&gt; 0.00344792&#10;鹿兒島火山 =&gt; 0.00344792&#10;高松商高校 =&gt; 0.00344792&#10;新潟經營大學 =&gt; 0.00344792&#10;琵琶湖成蹊體育大學 =&gt; 0.00344792&#10;岐阜經濟大學 =&gt; 0.00344792&#10;京都產業大學 =&gt; 0.00344792&#10;山梨學院大學附屬高校 =&gt; 0.00344792&#10;德島市立高中 =&gt; 0.00344792&#10;SRC廣島 =&gt; 0.00344792&#10;上田魂 =&gt; 0.00344792&#10;熊本教員蹴友團 =&gt; 0.00344792&#10;神戶勝利船 =&gt; 0.0104609&#10;甲府風林 =&gt; 0.018178&#10;湘南比馬 =&gt; 0.0251236&#10;千葉市原 =&gt; 0.0287366&#10;磐田山葉 =&gt; 0.0296735&#10;長崎成功丸 =&gt; 0.0297321&#10;松本山雅 =&gt; 0.0319914&#10;SC相模原 =&gt; 0.0393495&#10;仙台維加泰 =&gt; 0.0454915&#10;佐川急便滋賀 =&gt; 0.0509258&#10;大阪櫻花 =&gt; 0.0533919&#10;金澤薩維根 =&gt; 0.0565782&#10;鳥棲砂岩 =&gt; 0.0660711&#10;佐川印刷 =&gt; 0.0705519&#10;川崎前鋒 =&gt; 0.0787064&#10;FC仙台 =&gt; 0.0839376&#10;八戶雲羅里 =&gt; 0.0875501&#10;沼津青藍 =&gt; 0.0916813&#10;名古屋八鯨 =&gt; 0.0922489&#10;柏雷素爾 =&gt; 0.0948848&#10;橫濱水手 =&gt; 0.0971081&#10;FC東京 =&gt; 0.108155&#10;廣島三箭 =&gt; 0.118006&#10;町田澤維亞 =&gt; 0.123341&#10;浦和紅鑽 =&gt; 0.12816&#10;FC本田 =&gt; 0.132533&#10;鹿兒島聯 =&gt; 0.143419&#10;大阪飛腳 =&gt; 0.150023&#10;鹿島鹿角 =&gt; 0.150961&#10;長野帕塞羅 =&gt; 0.183793&#10;山口雷法 =&gt; 0.194005&#10;```&#10;&#10;```&#10;The bigger the rating is, the stronger the team is.&#10;As the code implements an online algorithm, one can plot the ratings of teams against the dates:&#10;(The first 100 data points are not plotted)&#10;&#10;$" src="svgs/f2cf9681e804572ca858808995924bce.png" align="middle" width="769.15905pt" height="1191.77982pt"/> python3 jleague_rating.py 鹿島鹿角 浦和紅鑽 清水心跳
```

![Figure_1.png](Figure_1.png?raw=true "Figure 1")

# Data

The data is stored in `japan_soccer.csv`. It consists of all matches among Japan football teams between 2005 Jan 1 to 2015 Dec 31. The data was collected from various sources by me.

The meaning of the field as follows

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
