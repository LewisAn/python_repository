#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Mar 30 11:23:02 2019

@author: apple
"""
from random import choice
from matplotlib import pyplot as p
class RandomWalK():
    def __init__(self, points=100):
        self._points = points
        self._x_values = [1] # start with 1
        self._y_values = [1] # start with 1
    
    def walk(self):
        while len(self._x_values) < self._points:
            x_direction = choice([1, -1])
            x_distance = choice([1, 2])
            y_direction = choice([1, 2, 3, 4])
            y_distance = choice([1, 2, 3, 4])
            x_step = x_direction * x_distance
            y_step = y_direction * y_distance
            if x_step == 0 or y_step == 0:
                continue
            x_next_value = self._x_values[-1] + x_step
            y_next_value = self._y_values[-1] + y_step
            self._x_values.append(x_next_value)
            self._y_values.append(y_next_value)
            
rw = RandomWalK()
rw.walk()

p.scatter(rw._x_values, rw._y_values)
p.show()
            
            
        