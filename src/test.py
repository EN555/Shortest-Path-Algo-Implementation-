# -*- coding: utf-8 -*-
"""
Created on Mon Dec 28 20:15:22 2020

@author: nir son
"""
import heapq
import copy

class A:
    def __init__(self):
        self.a = 23
    def __str__(self):
        return str(self.a)
class B:
    def __init__(self , aa):
        self.a = aa
    def __str__(self):
        return str(self.a)


if __name__ == '__main__':
   str1 = "1,2,3"
   tuple1 = tuple([float(x) for x in str1.split(',')])
   print(tuple1)