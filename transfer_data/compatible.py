# -*- coding: utf-8 -*-
"""
Created on Thu Mar 24 19:01:54 2022

@author: Christopher S. Francis

@version: Python 3.10.2
"""



from person import *


people = [Person("Charlie", 22, "Charlestown"),
          Person("Sally", 38, "Salem"), 
          Person("Alan", 16, "New Albany"), 
          Person("Jeff", 22, "Jeffersonville")]



##################  CSV

import csv

with open("dataFile1.csv", "w") as csvHandler:
    writer = csv.writer(csvHandler)
    for p in people:
        writer.writerow([p.name, p.age, p.town])
        

with open("dataFile1.csv", "r") as csvHandler:
    reader = csv.reader(csvHandler)
    for row in reader:
        if len(row) != 0:
            print(row)



######################  JSON

import json

with open("dataFile1.json", "w") as jsonHandler:
    for p in people:
        jsonHandler.write(json.dumps({"name":p.name, "age": p.age, "town": p.town}) + "\n")

with open("dataFile1.json", "r") as jsonHandler:
    for line in jsonHandler:
        print(json.loads(line.strip()))



f"this string is formatted"

b"this string is unicode"















########################  WHITE SPACE FOR SCROLLING  ###################