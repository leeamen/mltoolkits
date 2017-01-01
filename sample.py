#!/usr/bin/python
#coding:utf-8

from mltoolkits import *
import mltoolkits.mythreadpool as tp
import logging
import sys

if __name__ == '__main__':
  logger = logging.getLogger(sys.argv[0])
  
  #args:用户数据，可以自定义
  def process(args):
    logger.info('task %d is finished!', args['taskid'])
  
  #创建线程池
  threadpool = tp.MyThreadPool(2)
  #任务分发
  for i in range(1,10):
    threadpool.DispatchTask(process, {'taskid':i})
  #线程池销毁
  threadpool.Destroy()

