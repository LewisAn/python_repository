#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Mar 30 10:56:49 2019

@author: apple
"""
import pandas as p
import csv
"""
index city continent population climate
1 Beijing Asia 4000 warm
2 Brisbane Australia 200 hot
3 Alaska America 100 cold
4 Mumbuy India 300 moderate
"""
# Four columns of data in csv
index = [1, 2, 3, 4]
city = ['Beijing', 'Brisbane', 'Alaska', 'Mumbuy']
continent = ['Asia', 'Australia', 'America', 'India']
population = [4000, 200, 100, 300]
climate = ['warm', 'hot','cold','moderate']

data_frame = p.DataFrame({'index':index,
                          'city':city,
                          'population':population,
                          'climate':climate})

data_frame.to_csv('111.csv', index=False)

filename = '111.csv'

with open(filename) as f:
    reader = csv.reader(f)
    header_row = next(reader)
    print(header_row)
