# -*- coding: utf-8 -*-
"""
Created on Thu Mar 24 17:47:21 2022

@author: Christopher S. Francis

@version: Python 3.10.2
"""


class Person():
    def __init__(self, name, age, town):
        self.name = name
        self.age = age
        self.town = town
        
    def __str__(self):
        return self.name