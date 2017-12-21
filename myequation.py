#/usr/bin/python
#coding:utf8

import numpy as np
def Cosine(x, y):
  return 1.0*np.dot(x, y)/np.sqrt(np.dot(x,x))/np.sqrt(np.dot(y,y))
def Sigmoid(x):
  return 1.0 / (1.0 + np.exp(-1.0 * x))
def SigmoidGradient(x):
  return Sigmoid(x) * (1 - Sigmoid(x))

#平方误差,2范式的正则化项
def SquareErrorFunction2F(target_matrix_y, output_matrix_y, weights, lamda):
  m = len(target_matrix_y)
  err = target_matrix_y - output_matrix_y
  errors = 1.0/(2.0*m) * np.sum(err * err) + lamda*1.0/(2.0*m)*np.sum(weights * weights)
  return errors

def LogisticErrorFunction2F(target_matrix_y, output_matrix_y, weights, lamda):
  m = len(target_matrix_y)
  vector_j = target_matrix_y * np.log(output_matrix_y) + (1.0 - target_matrix_y) * np.log(1.0 - output_matrix_y)
  errors = -1.0/m*np.sum(vector_j) + lamda/(2.0*m) * np.sum(weights * weights)
  return errors

def RandomSample(size, a, b):
  epsilon_init = 0.12;
  arr = (b - a) * np.random.random_sample(size) + a
  return arr * epsilon_init * 2 - epsilon_init

import math
def GaussFunc(x, dimension, mu, sigma):
  inv = np.linalg.inv(sigma)
  e = -0.5 * np.dot(x - mu, inv)
  e = np.dot(e, (x-mu).T)
  re = 1./np.sqrt((2.*math.pi)**dimension) * 1./np.sqrt(np.linalg.det(sigma)) * np.exp(e)
  if x.ndim <= 1:return re
  else:return np.diag(re)

if __name__ == '__main__':
  print( Cosine(np.array([-1,-2]), np.array([1,2])))
  print( SigmoidGradient(np.array([-1,-2])))
  print( SquareErrorFunction2F(np.array([[0,1], [1,0]]), np.array([[0.5,0.5], [0.5,0.5]]), np.array([1,2,3]), 1))
  print( LogisticErrorFunction2F(np.array([[0,1], [1,0]]), np.array([[0.5,0.5], [0.5,0.5]]), np.array([1,2,3]), 1))
  print( RandomSample((2,3), 0, 1))
  print( GaussFunc(np.array([0,0]), 2, [0, 0], np.array([[1.,0],[0.,1]])))
  print( GaussFunc(np.array([[0,0.],[1,2.]]), 2, [0, 0], np.array([[1.,0],[0.,1]])))

