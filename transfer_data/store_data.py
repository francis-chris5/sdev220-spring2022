# -*- coding: utf-8 -*-
"""
Created on Tue Mar 29 19:06:17 2022

@author: Christopher S. Francis

@version: Python 3.10.2
"""

from person import *

people = [Person("Charlie", 22, "Charlestown"),
          Person("Sally", 38, "Salem"), 
          Person("Alan", 16, "New Albany"), 
          Person("Jeff", 22, "Jeffersonville")]


individual = Person("Becky", 32, "Borden")



################## BINARY FILE


import pickle ## old verb not used anymore, we typically say "serialize"


with open("dataFile2.per", "wb") as binHandler:
    pickle.dump(people, binHandler)
    
with open("dataFile2.per", "rb") as binHandler:
    stuff = pickle.load(binHandler)
    print(stuff[2].age)





























###############################  