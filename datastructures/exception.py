# -*- coding: utf-8 -*-
"""
Created on Thu Apr  7 18:10:03 2022

@author: Christopher S. Francis

@version: Python 3.10.2
"""



from tkinter.filedialog import *

#filepath = askopenfilename()

filepath = "employees.txt"


def sayHi(name):
    print("Why hello there " + str(name))

try:
    with open(filepath, "r") as fromFile:
        for line in fromFile:
            name = line.split(",")[0]
            sayHi(name)
    print("worked like it was supposed to...")
except FileNotFoundError:
    data = "sally,22.34\nbob,17.34\ndavid,17.34\nbecky,23.45"
    with open(filepath, "w") as toFile:
        toFile.write(data)
    lines = data.split("\n")
    for l in lines:
        name = l.split(",")[0]
        sayHi(name)
   