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
        self._x_values = [0] # start with 1
        self._y_values = [0] # start with 1

    def walk(self):
        
        while len(self._x_values) < self._points:
            x_direction = choice([0, 1, 2])
            x_distance = choice([0, 1, 2])
            y_direction = choice([0, 1, 2, 3, 4, 5, 6, 7, 8, 9])
            y_distance = choice([0, 1, 2, 3, 4])
            x_step = x_direction * x_distance # 此刻模拟出的x坐标
            y_step = y_direction * y_distance # 此刻模拟出的y坐标
            if x_step == 0 or y_step == 0:
                continue
            x_next_value = self._x_values[-1] + x_step# 下一个x点坐标 
            y_next_value = self._y_values[-1] + y_step# 下一个y点坐标
            self._x_values.append(x_next_value)
            self._y_values.append(y_next_value)




random_walk = RandomWalK()
random_walk.walk()

p.scatter(random_walk._x_values, random_walk._y_values,s=50, c='black')
p.plot()
p.axis([0, 2000, 0, 10000])
p.show()

            
        