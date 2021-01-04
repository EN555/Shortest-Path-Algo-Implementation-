# -*- coding: utf-8 -*-
"""
Created on Mon Dec 28 20:15:22 2020

@author: nir son
"""
import heapq
import copy
import math
import numpy as np
import matplotlib.pyplot as plt
import networkx as nx
import time
from threading import *


def is_prime(n:int) -> bool:
    
    if n==0 or n==1 or n==-1:
        return False
    
    for i in range(2,int(math.sqrt(abs(n))) + 1):
        if((n % i) == 0):
            return False
    return True



if __name__ == '__main__':
    x = []
    for i in range(-10000,10000):
        if is_prime(i):
            x.append(i)
    plt.scatter(x,x,s=0.1)
    print(x)
    #print(is_prime(15))
