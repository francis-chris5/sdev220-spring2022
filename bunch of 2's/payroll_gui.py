# -*- coding: utf-8 -*-
"""
Created on Tue Feb 22 18:31:56 2022

@author: Christopher S. Francis

@version: Python 3.10.2
"""

import sys
sys.path.insert(0, "C:\\Users\\franc\\Documents\\delete\\git-stuff\\pyOffice")


import tkinter as tk
from employees import *

employees = [
    Laborer(name="Bob", rate=17.34, vacationDays = "july 4", department="labor"),
    Clerical(name ="Sally", rate = 19.87, vacationDays = "whenever", access="VIP"),
    UpperMgmt(name="Becky", salary = 43210, bonus="20% of new sales")
    ]

REGULAR_TIME = 40

def GrossPay(event):
    hours=35
    choice = int(txtEmployee.get())
    employee = employees[choice]
    if isinstance(employee, Manager):
        hours = REGULAR_TIME
    if hours <= REGULAR_TIME:
        gross = hours * employee.getRate()
    else:
        gross = REGULAR_TIME * employee.getRate() + 1.5 * (hours - REGULAR_TIME) * employee.getRate()
    lblInstructions["text"] = gross








gui = tk.Tk()
gui.geometry("765x432")
gui.title("Payroll Thing")



mnMain = tk.Menu(gui)
mnPay = tk.Menu(mnMain, tearoff=0)
mnPay.add_command(label="Gross Pay", command= lambda : GrossPay(None))
mnMain.add_cascade(label="Payroll", menu=mnPay)


lblInstructions = tk.Label(gui, text="choose employee 0 - 2:")
txtEmployee = tk.Entry(gui)

gui.config(menu=mnMain)

lblInstructions.pack(padx=10, pady=45)
txtEmployee.pack(padx=10, pady=23)






#guard
if __name__=="__main__":
    gui.mainloop()
    



