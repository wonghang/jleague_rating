# jleague_rating
Japan J League Ratings computed from eigenvectors

This code computes ratings from raw data of Japan J League.

# The Algorithm

The algorithm is based on 

> Brent, Richard P. "Note on Computing Ratings from Eigenvectors." * *arXiv preprint* * arXiv:[1005.0762](https://arxiv.org/abs/1005.0762) (2010).

The problem is as follow:

There are <img alt="$n$" src="svgs/55a049b8f161ae7cfeb0197d75aff967.png" align="middle" width="9.867000000000003pt" height="14.155350000000013pt"/> players playing among each other in a zero-sum game for several times. Assume a WIN score 1 mark, a DRAW score 0.5 marks and a LOSE scores 0 marks. We obtained a score matrix <img alt="$s_{ij}$" src="svgs/8184020a45b4be8100982ccf94eb83a1.png" align="middle" width="18.461025pt" height="14.155350000000013pt"/>.

We want to compute a rating <img alt="$r_i$" src="svgs/3cf87ea38a615ed99e0232f8ed9431fe.png" align="middle" width="12.067275000000004pt" height="14.155350000000013pt"/> for each player <img alt="$i$" src="svgs/77a3b857d53fb44e33b53e4c8b68351a.png" align="middle" width="5.663295000000005pt" height="21.683310000000006pt"/> from the score matrix <img alt="$s_{ij}$" src="svgs/8184020a45b4be8100982ccf94eb83a1.png" align="middle" width="18.461025pt" height="14.155350000000013pt"/> that capture the relative strength of the player <img alt="$i$" src="svgs/77a3b857d53fb44e33b53e4c8b68351a.png" align="middle" width="5.663295000000005pt" height="21.683310000000006pt"/>

To start with, we assume the rating <img alt="$r_i$" src="svgs/3cf87ea38a615ed99e0232f8ed9431fe.png" align="middle" width="12.067275000000004pt" height="14.155350000000013pt"/> and <img alt="$r_j$" src="svgs/212f899c5235a861a1f6146dc8d1582f.png" align="middle" width="13.520925000000005pt" height="14.155350000000013pt"/> would capture the expected score of a player <img alt="$i$" src="svgs/77a3b857d53fb44e33b53e4c8b68351a.png" align="middle" width="5.663295000000005pt" height="21.683310000000006pt"/> in a game against player <img alt="$j$" src="svgs/36b5afebdba34564d884d347484ac0c7.png" align="middle" width="7.710483000000004pt" height="21.683310000000006pt"/> as <img alt="$f(r_i - r_j)$" src="svgs/3b03c5390eb15e78ef471bd6b3254bcc.png" align="middle" width="69.92601pt" height="24.65759999999998pt"/> for some function <img alt="$f: \mathbb{R} \to [0,1]$" src="svgs/eee6982d58163a355d800d004a5530fc.png" align="middle" width="93.8355pt" height="24.65759999999998pt"/>.

Under some reasonable assumptions, we can model <img alt="$f$" src="svgs/190083ef7a1625fbc75f243cffb9c96d.png" align="middle" width="9.817500000000004pt" height="22.831379999999992pt"/> as a logistic function <img alt="$f(z) = \frac{1}{1+e^{-cz}}$" src="svgs/4db44e8713c4b0fd70cfe00e0962f393.png" align="middle" width="98.770155pt" height="27.775769999999994pt"/> for some number <img alt="$c$" src="svgs/3e18a4a28fdee1744e5e3f79d13b9ff6.png" align="middle" width="7.113876000000004pt" height="14.155350000000013pt"/>

After some simplification, the solution of the problem reduces into an eigenvalue problem. The code computes the solution by power method.

The code implements an efficient sparse and online version of the algorithm (i.e., new data can be fed into the algorithm to update previously computed ratings). The code uses a python `dict` object to store the sparse score matrix.

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

Any **-1** in the data means missing data.

# API

# Example
