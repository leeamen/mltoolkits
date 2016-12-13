#!/usr/bin/python
#coding:utf8

import sys
import numpy as np
import mylog
import logging
def PCA(dataMat, topNfeat=9999999):
  meanVals = np.mean(dataMat, axis=0)
  meanRemoved = dataMat - meanVals #remove mean
  covMat = np.cov(meanRemoved, rowvar=0)
  eigVals,eigVects = np.linalg.eig(np.mat(covMat))
  eigValInd = np.argsort(eigVals)      #sort, sort goes smallest to largest
  eigValInd = eigValInd[:-(topNfeat+1):-1]  #cut off unwanted dimensions
  redEigVects = eigVects[:,eigValInd]    #reorganize eig vects largest to smallest
  lowDDataMat = meanRemoved * redEigVects#transform data into new dimensions
  reconMat = (lowDDataMat * redEigVects.T) + meanVals
  return lowDDataMat
#  return lowDDataMat, reconMat

if __name__ == '__main__':
  logger = logging.getLogger(sys.argv[0])
  logger.setLevel(logging.DEBUG)
  logger.debug('start...')
  #test
  vec = np.array([[1,2,3],[4,5,6.0]]) 
  low_vec = PCA(vec, 2)
  logger.debug('%s', low_vec)
