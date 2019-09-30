# jleague_rating
Japan J League Ratings computed from eigenvectors

This code compute ratings from raw data of Japan J League.
The algorithm is based on 

Brent, Richard P. "Note on Computing Ratings from Eigenvectors." __arXiv preprint__ arXiv:[1005.0762](https://arxiv.org/abs/1005.0762) (2010).

# Data

The data is stored in `japan_soccer.csv`. It consists of all matches among Japan football teams between 2005 Jan 1 to 2015 Dec 31. The data was collected from various sources by me.

The meaning of the field as follows

| field | meaning |
| --- | --- |
| date | Date of the football match |
| league | League of the match. JD1=J1 League
JD2=J2 League
JD3=J3 League
JDP=Extra matches in J. League (normally for seeking second runner-up)
JEC=The Emperor's Cup (サッカー天皇杯)
JFL=Japan Football League (for amateur)
JLC=J. League Cup
JSC=Japan Super Cup (富士ゼロックス スーパーカップ)
1JSTL=Japan Satellite League |

<p align="center"><img alt="$$&#10;\int_0^{\infty} \frac{\sin(x)}{x} \mbox{d} x = \frac{\sqrt{\pi}}{2}&#10;$$" src="https://rawgit.com/in	git@github.com:wonghang/jleague_rating/None/svgs/461b521e0c9a8623a44d18d090fa598b.png" align="middle" width="145.48973999999998pt" height="38.595645pt"/></p>
