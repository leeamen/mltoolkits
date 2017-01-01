#!/usr/bin/python
#coding:utf-8
import numpy as np
from matplotlib.pyplot import *
from matplotlib.mlab import *
def Figure():
  figure()
def Plot2DLine(x,y, xla, yla):
  #画图
#  plot(x[pos], y[pos], '+r', markersize = 5)
#  plot(x[neg], y[neg], 'xg', markersize = 3)
  xlabel(xla)
  ylabel(yla)
  plot(x, y)
def Show():
  show()
def Legend(arr):
  legend(arr)
def Title(tit):
  title(tit)

def ShowPictures(x):
  figure()
  x = x[np.random.permutation(len(x))[0:100]]
  for i in range(0,100):
    subplot(10, 10, i+1)
    axis('off')
    imshow(x[i].reshape(20,20).T, cmap='gray')

  show()

def ShowPicture(x, i):
#  show_data = x[np.random.permutation(5000)[0:100],:]
  axis('off')
  imshow(x[i].reshape(20,20).T, cmap='gray')
  show()

