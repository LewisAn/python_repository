#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Mar 30 12:39:25 2019

@author: apple
"""

import matplotlib.pyplot as p
from random import randint
for i in range(1000):
    x = randint(0, 100)
    y = randint(0, 100)
    p.scatter(x, y, s=5, c='red', edgecolors=None)
#    x = i
#    y = i
#    p.scatter(x, y, s=5, c='red', edgecolors=None)



p.axis([0, 100, 0, 100])
p.xlabel("x")
p.ylabel("y")
p.plot()
p.show()

