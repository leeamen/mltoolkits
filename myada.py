#!/usr/bin/python
#coding:utf8
import numpy as np
import os
import sys
import myfunc
import myrandom

'''
需要实现train_and_return_model_callback回调函数，
训练样本并返回模型
'''

def Adaboost(x, y, x1, y1, num_classifier, train_and_return_model_callback, param):
  #初始化权重
  N = len(x)
  k = num_classifier

  weight = np.array([1.0/N] * N, dtype = np.float)
  alpha = np.zeros(k, dtype = np.float)
  Z = np.zeros(k, dtype = np.float)
  classifiers = []
  i = 0
  while i < k:
    (train_x, train_y) = myrandom.GetRepeatSample(x, y)
    classifer = train_and_return_model_callback(train_x, train_y, param)
    classifiers.append(classifer)
    pred = classifer.Predict(train_x)
    epsilon = 1.0/N * np.dot(weight, np.array(pred == train_y, dtype = np.float))
    if epsilon > 0.5:
      weight = np.array([1.0/N] * N, dtype = np.float)
      continue
    #更新权值
    alpha[i] = 1.0/2 * np.log((1-epsilon)/epsilon)
    tmp = np.exp(alpha[i]) * (pred != train_y) + np.exp(-1.0 * alpha[i])*(pred == train_y)
    Z[i] = np.sum(tmp * weight)
    weight = weight / Z[i] * tmp
    i+=1
  #计算最终标签
  preds = {}
  for i in range(0, len(classifiers)):
    preds[i] = classifiers[i].Predict(x1)

  N = len(x1)
  args = np.empty((0, N), dtype = np.float)
  for i in range(0, param['class_num']):
    arg = np.zeros(N, dtype = np.float)
    for j in range(0, len(classifiers)):
      arg += alpha[j] * (preds[j] == i)
    args = np.vstack((args, arg))

  final_y = myfunc.VArgmax(args, N)
  acc = 1.0*sum(final_y == y1) / len(y1)
  return acc

if __name__ == '__main__':
  pass
