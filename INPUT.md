# jleague_rating
Japan J League Ratings computed from eigenvectors

This code computes ratings from raw data of Japan J League.

# The Algorithm

The algorithm is based on 

> Brent, Richard P. "Note on Computing Ratings from Eigenvectors." * *arXiv preprint* * arXiv:[1005.0762](https://arxiv.org/abs/1005.0762) (2010).

The problem is as follow:

There are $n$ players playing among each other in a zero-sum game for several times. Assume a WIN score 1 mark, a DRAW score 0.5 marks and a LOSE scores 0 marks. We obtained a score matrix $s_{ij}$.

We want to compute a rating $r_i$ for each player $i$ from the score matrix $s_{ij}$ that capture the relative strength of the player $i$

To start with, we assume the rating $r_i$ and $r_j$ would capture the expected score of a player $i$ in a game against player $j$ as $f(r_i - r_j)$ for some function $f: \mathbb{R} \to [0,1]$.

Under some reasonable assumptions, we can model $f$ as a logistic function $f(z) = \frac{1}{1+e^{-cz}}$ for some number $c$

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
