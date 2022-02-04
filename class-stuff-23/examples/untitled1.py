# -*- coding: utf-8 -*-
"""
Created on Thu Feb  3 18:53:52 2022

@author: c.s.francis

@version: Python 3.10.2

@summary: test case for payroll module
"""

import sys
sys.path.insert(0, 'C:\\Users\\franc\\Documents\\delete\\git-stuff\\class-stuff-23\\pyOffice')

import payroll



emp1Name = "Bob"
emp1Rate = 17.34
emp2Name = "Sally"
emp2Rate = 19.87
emp3Name = "Becky"
emp3Rate = 27.78
emp4Name = "David"
emp4Rate = 17.34

counter = 1
while counter < 5:
    if counter == 1:
        gross = payroll.GrossPay(emp1Name, emp1Rate)
        net = payroll.Taxes(gross)
        print(f"{emp1Name} made ${net} this period.")
    elif counter == 2:
        gross = payroll.GrossPay(emp2Name, emp2Rate)
        net = payroll.Taxes(gross)
        print(f"{emp2Name} made ${net} this period.")
    elif counter == 3:
        gross = payroll.GrossPay(emp3Name, emp3Rate)
        net = payroll.Taxes(gross)
        print(f"{emp3Name} made ${net} this period.")
    elif counter == 4:
        gross = payroll.GrossPay(emp4Name, emp4Rate)
        net = payroll.Taxes(gross)
        print(f"{emp4Name} made ${net} this period.")
    counter += 1
    

