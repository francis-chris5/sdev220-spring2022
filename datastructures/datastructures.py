# -*- coding: utf-8 -*-
"""
Created on Thu Apr  7 19:06:42 2022

@author: Christopher S. Francis

@version: Python 3.10.2
"""


## linked list
class LLNode():
    def __init__(self, element):
        self.element = element
        self.next = None
        
    def __str__(self):
        return "This node holds " + str(self.element)
    



## custom linked list built into object

class Crew():
    def __init__(self, name, position, rate):
        self.name = name
        self.position = position
        self.rate = rate
        self.next = None
        
    def __str__(self):
        return str(self.name) + " is the " + str(self.position) + " and makes " + str(self.rate) + " per hour."
        
    
    






class Stack():
    def __init__(self):
        self.__stuff = []
    
    def push(self, item):
        self.__stuff.insert(0, item)
    
    
    def pop(self):
        top = self.__stuff[0]
        self.__stuff.remove(top)
        return top
    
    
    def peek(self):
        return self.__stuff[0]
    
    def size(self):
        return len(self.__stuff)
    
    
    def __str__(self):
        return str(self.__stuff)



class Queue():
    def __init__(self):
        self.__stuff = []
        
        
    ## or enqueue
    def poll(self, item):
        self.__stuff.append(item)
    
    
    ## or dequeue ("deck")
    def remove(self):
        top = self.__stuff[0]
        self.__stuff.remove(top)
        return top
    
    
    
    def peek(self):
        return self.__stuff[0]
    
    
    def size(self):
        return len(self.__stuff)
    
    def __str__(self):
        return str(self.__stuff)
        
    
    
















#############################
    
