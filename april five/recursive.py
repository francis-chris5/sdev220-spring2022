# -*- coding: utf-8 -*-
"""
Created on Tue Apr  5 19:06:18 2022

@author: Christopher S. Francis

@version: Python 3.10.2
"""



from os import *
from os.path import *

import time

path = "C:/Users/franc/Documents"

stuff = [folder for folder in listdir(path) if isdir(join(path, folder))]

def forward(stuff):
    if len(stuff) == 0:
        return
    else:
        print(stuff[0])
        forward(stuff[1:])
        
def backward(stuff):
    if len(stuff) == 0:
        return
    else:
        print(stuff[-1])
        forward(stuff[:-1])
   
    
print("Recursive...")
current = time.time_ns()
forward(stuff)
duration = time.time_ns() - current
print("time: " + str(duration))

print()
print()



print("for each loop...")
current = time.time_ns()
for s in stuff:
    print(s)
duration = time.time_ns() - current
print("time: " + str(duration))




print()
print()
print()


backward(stuff)



current = time.time_ns()

exec(open("homework.py").read())


duration = time.time_ns() - current
print("time: " + str(duration))
















########################################