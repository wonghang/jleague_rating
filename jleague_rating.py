#!/usr/bin/python3
# -*- coding: utf-8 -*-
import datetime
import csv
import operator
import sys
from collections import deque

import numpy as np
import matplotlib.pyplot as plt
from matplotlib import dates
from matplotlib.font_manager import FontProperties
import pandas as pd

from brent_rating import *

def convert_date(d):
    yy = int(d[0:4])
    mm = int(d[4:6])
    dd = int(d[6:8])
    return dates.date2num(datetime.datetime(yy,mm,dd))

def loop_through():
    header = None

    br = online_brent_rating()
    last_date = None
    pending = deque()

    def _flush():
        if len(pending) > 0:
            for (home,away,S) in pending:
                br.new_name(home)
                br.new_name(away)
            br.start()
            for (home,away,S) in pending:
                br.add(home,away,S)
            br.commit(decay=0.99)
            pending.clear()

    data = pd.read_csv("japan_soccer.csv",dtype={
        "date": str,
        "league": str,
        "home": str,
        "away": str,
        "neutral": int,
        "full-home": int,
        "full-away": int,
        "half-home": int,
        "half-away": int,
        "corner-home": int,
        "corner-away": int,
        "redcard-home": int,
        "redcard-away": int,
    })
    for _,row in data.iterrows():
        today = row['date']
        if today != last_date:
            if last_date is not None:
                _flush()
                yield (last_date,br)
            last_date = today
        else:
            home = row['home']
            away = row['away']
            home_score = row['full-home']
            away_score = row['full-away']
            
            if home_score > away_score:
                S = 1
            elif home_score < away_score:
                S = -1
            else:
                S = 0
            pending.append([home,away,S])
    if last_date is not None:
        _flush()
        yield (last_date,br)
    
def main():
    if len(sys.argv) == 1:
        print("%s (team name 1) (team name 2) ..." % sys.argv[0])
        sys.exit(1)
    else:
        teams = sys.argv[1:]
        
    ignore_first = 100
    x = []
    y = []
    for (today,br) in loop_through():
        if ignore_first <= 0:
            x.append(convert_date(today))
            y.append([br[_] for _ in teams])
        else:
            ignore_first -= 1
        
    plt.figure()
    plt.plot_date(x,y,'-')

    font_prop = FontProperties(family='Droid Sans Fallback')
    plt.legend(teams,prop=font_prop)
    plt.grid(True)
    plt.show()

if __name__ == "__main__":
    main()
