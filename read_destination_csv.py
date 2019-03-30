#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Mar 29 20:11:25 2019

@author: apple
"""
import csv
from matplotlib import pyplot as p

filename = 'destinations.csv'

with open(filename) as f:
    reader = csv.reader(f)
    header_row = next(reader)
    spring_factors = list()
    summer_factors = list()
    for row in reader:
        spring_factors.append(float(row[6]))
    x_values = list(range(50))
    y1_values = spring_factors
    p.plot(x_values, y1_values, c='red')
    p.xlabel("destination index")
    p.ylabel("spring season factors")
    p.savefig('1.png')
    
        