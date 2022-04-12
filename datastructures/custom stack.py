# -*- coding: utf-8 -*-
"""
Created on Tue Apr 12 19:14:15 2022

@author: Christopher S. Francis

@version: Python 3.10.2
"""


filepath = "employees.txt"




   
    

class Crew():
    def __init__(self):
        self.__folks = []
        
    def PushFolks(self):
        try:
            with open(filepath, "r") as fromFile:
                for line in fromFile:      
                    self.__folks.insert(0, line.split(","))
        except FileNotFoundError:
            data = "sally,22.34\nbob,17.34\ndavid,17.34\nbecky,23.45"
            with open(filepath, "w") as toFile:
                toFile.write(data)
            lines = data.split("\n")
            for l in lines:
                self.__folks.insert(0, l.split(","))
    
    
    def PayrollPop(self):
        if len(self.__folks) == 0:
            return "That's all for now..."
        else:
            current = self.__folks[0]
            self.__folks.remove(current)
            hours = float(input("Please enter " + str(current[0]) + "'s hourse worked: "))
            gross = float(current[1]) * hours
            return f"{current[0]} made ${gross} this pay period."
        
        
#del current
#gc.collect()
        




























#####################################################