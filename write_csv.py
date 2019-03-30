#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Mar 30 10:56:49 2019

@author: apple
"""
import pandas as p

a = [1,2,3]
b = [1,2,3]

dataframe = p.DataFrame({'a':a, 'b':b})
dataframe.to_csv("test.csv", index=False) 