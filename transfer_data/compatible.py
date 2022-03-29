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





########################  XML

# people = [Person("Charlie", 22, "Charlestown"),
#           Person("Sally", 38, "Salem"), 
#           Person("Alan", 16, "New Albany"), 
#           Person("Jeff", 22, "Jeffersonville")]

nicknames = ["big C", "sal", "alien", "elf"]
import xml.etree.ElementTree as et


## for i in range(len(peopl))

root = et.Element("people")
for count, p in enumerate(people):
    branch = et.SubElement(root, "person")
    
    leaf1 = et.SubElement(branch, "name")
    leaf1.text = p.name
    leaf1.attrib = {"nickname": nicknames[count]}
    
    
    leaf2 = et.SubElement(branch, "age")
    leaf2.text = str(p.age)
    leaf3 = et.SubElement(branch, "town")
    leaf3.text = p.town
    
tree = et.ElementTree(root)


with open("dataFile1.xml", "wb") as xmlHandler:
    tree.write(xmlHandler)
    

newTree = et.parse("dataFile1.xml")

newRoot = newTree.getroot()

for i in range(len(newRoot)):
    for j in range(len(newRoot[i])):
        print(newRoot[i][j].tag + ": " + newRoot[i][j].text)
        print(newRoot[i][j].attrib)
    

    











########################  WHITE SPACE FOR SCROLLING  ###################