#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Mar 29 21:41:04 2019

@author: apple
"""

import matplotlib.pyplot as p

x_values = [1,2,3,4,5]
y1_values = [1,4,9,16,25]
y2_values = [1,2,3,4,5]

p.plot(x_values, y1_values)
p.plot(x_values, y2_values)
p.xlabel("x")
p.ylabel("y = x^2")
p.tick_params(axis='both', which='major', labelsize=14)

p.show()