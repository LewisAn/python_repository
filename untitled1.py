#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Mar 30 16:57:08 2019

@author: apple
"""

import matplotlib.pyplot as p
import random as r
#
for i in range(0, 100):
    x = r.randint(0, 500)
    y = r.randint(0, 500)
    p.scatter(x, y, s=5, c='black')

p.plot()
p.axis([0, 1000, 0, 1000])
p.show()