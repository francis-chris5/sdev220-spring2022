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



################################  SQLite ##############################################################################################################


# people = [Person("Charlie", 22, "Charlestown"),
#           Person("Sally", 38, "Salem"), 
#           Person("Alan", 16, "New Albany"), 
#           Person("Jeff", 22, "Jeffersonville")]

import sqlite3 as sql

db = sql.connect("dataFile2.db")

createQuery = "CREATE TABLE IF NOT EXISTS people(id INTEGER PRIMARY KEY AUTOINCREMENT, Name TEXT, Age INTEGER, Town TEXT);"


db.execute(createQuery)


for p in people:
    insertQuery = "INSERT INTO people(Name, Age, Town) VALUES(\""  + p.name + "\"," + str(p.age)  + ", \"" + p.town + "\");"
    cursor = db.execute(insertQuery)
    if cursor.rowcount >= 0:
        print("inserted some data")
    else:
        print("error inserting data")
    



selectQuery = "SELECT name, town FROM people WHERE age > 18;"

cursor = db.execute(selectQuery)

for row in cursor:
    print(row[0])
    
    
db.close()




















###############################  