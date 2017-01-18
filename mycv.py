#!usr/bin/python
#coding:utf8
import numpy as np

def CrossValidation(train_func, predict_func, x, y, fold):
  k = fold
  n = len(x) / k

  error_rate = 0.0
  for i in range(0, k):
    train_x = x[i*n :(i+1)*n, :]
    test_x = np.vstack((x[0:i*n, :], x[(i+1)*n:, :]))
    train_y = y[i*n : (i+1)*n]
    test_y = np.hstack((y[0: i*n], y[(i+1)*n:]))

#    logger.debug('train_x:%s,test_x:%s,train_y:%s,test_y:%s',train_x.shape,test_x.shape,train_y.shape,test_y.shape)
    train_func(train_x, train_y)
    pred = predict_func(test_x)
    error_rate += 1.0 * sum(pred != test_y)/len(test_y)
   # print len(test_y),sum(pred != test_y),error_rate
#  logger.info('10折交叉验证平均准确率:%f', 1.0 - error_rate / k)
  return (1.0 - error_rate / k)

if __name__ == '__main__':
  pass
