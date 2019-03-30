# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import csv
from matplotlib import pyplot as p
from datetime import datetime

filename = 'sitka_weather_07-2014.csv'

with open(filename) as f:
    reader = csv.reader(f)
    header_row = next(reader)
#    temp = next(reader)
    highs = []
#    dates = []
    for row in reader:
#        current_date = datetime.strptime(row[0], "%Y-%m-%d")
        highs.append(int(row[6]))
#        dates.append(current_date)
    print(highs)
#    print(dates)
    fig = p.figure(dpi=128, figsize=(10, 6))
    p.plot(highs, c='red')
    p.title("Temp")
#    fig.autofmt_xdate()
    p.xlabel("", fontsize=16)
    p.ylabel("Temperature (f)", fontsize=10)
    p.tick_params(axis="both", which='major', labelsize=16)
#    p.savefig('2.png')
    