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
| league | League of the match |
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

Any *-1* in the data means a missing data

<p align="center"><img alt="$$&#10;\int_0^{\infty} \frac{\sin(x)}{x} \mbox{d} x = \frac{\sqrt{\pi}}{2}&#10;$$" src="https://rawgit.com/in	git@github.com:wonghang/jleague_rating/None/svgs/461b521e0c9a8623a44d18d090fa598b.png" align="middle" width="145.48973999999998pt" height="38.595645pt"/></p>
