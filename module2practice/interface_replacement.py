# -*- coding: utf-8 -*-
"""
Created on Sun Jan 30 10:31:38 2022

a new line in the template

@author: Christopher S. Francis
"""


import abc

class Shape(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def area(self):
        return
    
    
    
class Square(Shape):
    def __init__(self, side):
        self.side = side
        
    def area(self):
        return self.side * self.side
    

class Rectangle():
    def __init__(self, length, width):
        self.width= width
        self.length = length
        
    def coverage(self):
        return self.width * self.length
    

#Shape.register(Square)
#Shape.register(Rectangle)
"""
 would not be able to do this in an interface --probably don'e show in class, 
 but this is as close as we have in python
"""

cubeFace = Square(4)
longThing = Rectangle(3, 4)

if isinstance(cubeFace, Shape):
    print("I know the area of this thing...")
    print(cubeFace.area())
else:
    print("can't tell you what this thing is...")


if isinstance(longThing, Shape):
    print("this thing has an area method by a different name...")
    print(longThing.coverage())
else:
    print("no way to determine area from what I can tell...")
    





