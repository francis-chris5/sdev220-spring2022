# -*- coding: utf-8 -*-
"""
Created on Thu Feb  3 18:53:52 2022

@author: c.s.francis

@version: Python 3.10.2

@summary: test case for payroll module
"""

import payroll
from employees import *



emp1 = Laborer(name="Bob", rate=17.34, vacationDays = "july 4", department="labor")
emp2 = Clerical(name ="Sally", rate = 19.87, vacationDays = "whenever", access="VIP")
emp3 = UpperMgmt(name="Becky", salary = 43210, bonus="20% of new sales")


counter = 1
while counter < 4:
    if counter == 1:
        gross = payroll.GrossPay(emp1)
        net = payroll.Taxes(gross)
        print(f"{emp1} made ${net} this period.")
    elif counter == 2:
        gross = payroll.GrossPay(emp2)
        net = payroll.Taxes(gross)
        print(f"{emp2} made ${net} this period.")
    elif counter == 3:
        gross = payroll.GrossPay(emp3)
        net = payroll.Taxes(gross)
        print(f"{emp3} made ${net} this period.")
    counter += 1
    

