# -*- coding: utf-8 -*-
"""
Created on Thu Feb 10 18:35:13 2022

@author: c.s.francis
@version: Python 3.10.2
"""

class Employee():
    def __init__(self, name, rate):
        self.__name = name
        self.__rate = rate
        
    def getName(self):
        return self.__name
    
    def setName(self, name):
        self.__name = name
        
    def getRate(self):
        return self.__rate
    
    def setRate(self, rate):
        self.rate = rate
        
    def __str__(self):
        return self.getName() + " makes " + str(self.getRate()) + " per hour."
    
    

class Laborer(Employee):
    def __init__(self, vacationDays, department, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.__vacationDays = vacationDays
        self.__department = department
        
        
    def getVacationDays(self):
        return self.__vacationDays
    
    def setVacationDays(self, vacationDays):
        self.__vacationDays = vacationDays
    
    def getDepartment(self):
        return self.__department
    
    def setDepartment(self, department):
        self.__department = department
    


class Clerical(Employee):
    def __init__(self, vacationDays, access, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.__vacationDays = vacationDays
        self.__access = access
        
    def getVacationDays(self):
        return self.__vacationDays
    
    def setVacationDays(self, vacationDays):
        self.__vacationDays = vacationDays
        
    def getAccess(self):
        return self.__access
    
    def setAccess(self, access):
        self.__access = access




class Manager(Employee):
    def __init__(self, salary, *args, **kwargs):
        super().__init__(rate=salary/52/40, *args, **kwargs)
        
        
        
class MiddleMgmt(Manager):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        
        
        
class UpperMgmt(Manager):
    def __init__(self, bonus, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.__bonus = bonus
        
        
    def getBonus(self):
        return self.__bonus
    
    def setBonus(self, bonus):
        self.__bonus = bonus
        
















        
        
        
        