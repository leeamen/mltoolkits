#!/usr/bin/python
#coding:utf8

import myrandom

x0, y0 = myrandom.Normal2D([1,2],[[1,1],[1,2]], 200)

x1, y1 = myrandom.Normal2D([10,20], [[4,1],[1,3]], 200)

import matplotlib.pyplot as plt

plt.plot(x0, y0, 'x')
plt.plot(x1, y1, 'o')
#plt.axis('equal')
plt.show()
