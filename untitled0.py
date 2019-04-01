#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Mar 30 16:19:11 2019

@author: apple
"""

import matplotlib.pyplot as p

# 再画一幅图，画 y = (3*x) ** 2 + 2 * x + 65
# 画一百个点，你需要用for loop
# 取一百个点你可以用for i in range(100)
# for i in range(100):
#    print(i)
# 程序会输出0到100，一百个数字
new_x = []
new_y = []
for i in range(100):
    x = i
    y = (3*x) ** 2 + 2 * x + 65
    new_x.append(x)
    new_y.append(y)

p.plot(new_x, new_y)
#p.axis([0, 10, 0, 10])
p.show()

