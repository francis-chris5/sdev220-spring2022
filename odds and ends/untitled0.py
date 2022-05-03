# -*- coding: utf-8 -*-
"""
Created on Tue May  3 17:59:17 2022

@author: Christopher S. Francis

@version: Python 3.10.2
"""


import gc
import random

myBigList = []

for i in range(1000000):
    if i%2==0:
        myBigList.append(random.random())
    else:
        myBigList.append(random.randint(0, 10000))
        
        
for n in myBigList:
    print(n)
    

del myBigList
gc.collect()


    
    
