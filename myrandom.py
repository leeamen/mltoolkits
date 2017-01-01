#!/usr/bin/python
#coding:utf8

import numpy as np
import sys
import random
import time
random.seed(time.time())

#高斯分布
def Normal(mu, sigma, size):
  return np.random.standard_normal(size) * sigma + mu
#2元高斯分布
def Normal2D(mu, cov, size):
  return np.random.multivariate_normal(mu, cov, size).T

#随机获取一个整数数组，元素区间[a, b)
def RandomIntArrayRepeat(size, a, b):
  return np.random.randint(a, b, size)

#ndarray抽样，矩阵返回ndarray,例如:
#>>> rd.sample(np.array([[1,2],[1,3],[1,4]]), 2)
#[array([1, 3]), array([1, 2])]
def RandomSampleList(x, size):
  re = np.empty((0, x.shape[1]), dtype = x.dtype)
  for e in random.sample(x, size):
    re = np.vstack((re, e))
  return re


if __name__ == '__main__':
  print Normal(1,10,(2,3))
  x,y = Normal2D([0, 0], [[1,0],[0,1]], 200)
  print x
  print y
  print RandomIntArrayRepeat(5, 0, 10)
  print RandomSampleList(np.array([[1,2.],[1,1],[1,4]]), 2)

  sys.exit(0)

  import matplotlib.pyplot as plt
  plt.plot(x, y, 'x')
  plt.show()

