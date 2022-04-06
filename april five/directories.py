# -*- coding: utf-8 -*-
"""
Created on Tue Apr  5 18:04:49 2022

@author: Christopher S. Francis

@version: Python 3.10.2
"""

from os import makedirs, rmdir, listdir
from os.path import isdir, isfile, join

# s1 = "C:/Users/franc"
# s2 = "Documents"
# print(join(s1, s2))


path = "C:/Users/franc/Documents"

for folder in listdir(path):
    try:
        if isdir(join(path, folder)):
            print(folder)         
            for f in listdir(join(path, folder)):
                print("      " + f)
    except:
        pass
    

