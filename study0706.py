# -*- coding: utf-8 -*-
"""
Created on Sat Jul  6 16:53:21 2019

@author: peng.zhou
"""

#类的学习
'''
today这个类的作用是输出今天的年月日
'''
#import datetime
#a="var"
#var="var1"
#class today(object):
#    def __init__(self,var):#self rec the var
#        self.year=datetime.datetime.now()
#        self.over="time over"
#        print("enter the __init__",self.year)
#    def __call__(self,ok):
#        print("enter the __call__ method")
#        return "1"
#    def imfinethanks(self,var):
#        print("enter the imfinethanks",var)
#im=today(var)
##print(type(im))
#
##print(im)
##print(im(var))
#print(im.imfinethanks(1))
#class test(object):
#    def __init__(self):
#        print(1)
#zh=test()

class test(object):
    def __init__(self,z1,z2):
        self.zh1=z1
        self.zh2=z2
        print("imok")
    def anyvar(self,b):
        delt=self.zh1
        print(delt,"delt")
print("im here")
zh=test(z1="z1",z2="z2")
zh.anyvar(b="var")        



        
        