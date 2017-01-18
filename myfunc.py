#/usr/bin/python
#coding:utf8

import numpy as np

#求每一列最大的值所在的行号,即标签,N,样例总数 (class_num * N)
def VArgmax(x, N):                                                                                          
  y = np.zeros(N, dtype = np.int)
  for i in range(0, N):
    try:
      y[i] = np.where(x[:,i] == np.max(x[:,i]))[0]
    except:
#      logger.debug('%s', np.where(x[:,i] == np.max(x[:,i]))[0])
#      logger.debug('%s', x[:,i])
      y[i] = np.where(x[:,i] == np.max(x[:,i]))[0][0]
  return y

#列的Argmax,所在的列号
def HArgmax(x, N):                                                                                          
  y = np.zeros(N, dtype = np.int)
  for i in range(0, N):
    try:
      y[i] = np.where(x[i,:] == np.max(x[i,:]))[0]
    except:
#      logger.debug('%s', np.where(x[:,i] == np.max(x[:,i]))[0])
#      logger.debug('%s', x[:,i])
      y[i] = np.where(x[i,:] == np.max(x[i,:]))[0][0]
  return y

if __name__ == '__main__':
  arr = np.array([[1,2,3],[2,3,2.5]])
  # 110
  print VArgmax(arr, 3)
  # 
  print HArgmax(arr, 2)
