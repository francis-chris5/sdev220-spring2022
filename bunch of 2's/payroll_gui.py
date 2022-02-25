# -*- coding: utf-8 -*-
"""
Created on Tue Feb 22 18:31:56 2022

@author: Christopher S. Francis

@version: Python 3.10.2
"""

import sys
sys.path.insert(0, "C:\\Users\\franc\\Documents\\delete\\git-stuff\\pyOffice")


import tkinter as tk
import tkinter.ttk as ttk
from employees import *

employees = [
    Laborer(name="Bob", rate=17.34, vacationDays = "july 4", department="labor"),
    Clerical(name ="Sally", rate = 19.87, vacationDays = "whenever", access="VIP"),
    UpperMgmt(name="Becky", salary = 43210, bonus="20% of new sales")
    ]

REGULAR_TIME = 40

def GrossPay(event):
    hours=35
    choice = int(txtBob.get())
    employee = employees[choice]
    if isinstance(employee, Manager):
        hours = REGULAR_TIME
    if hours <= REGULAR_TIME:
        gross = hours * employee.getRate()
    else:
        gross = REGULAR_TIME * employee.getRate() + 1.5 * (hours - REGULAR_TIME) * employee.getRate()
    lblBob["text"] = gross



def UpdateStatus(event, status):
    lblStatus["text"] = "Status: " + status





gui = tk.Tk()
gui.geometry("765x432")
gui.title("Payroll Thing")



mnMain = tk.Menu(gui)
mnPay = tk.Menu(mnMain, tearoff=0)
mnPay.add_command(label="Gross Pay", command= lambda : GrossPay(None))
mnMain.add_cascade(label="Payroll", menu=mnPay)


tbMain = tk.Frame(gui, border=3, relief="groove")
imgGrossPay = tk.PhotoImage(file="gross.png")
imgGrossPay = imgGrossPay.subsample(2) ##subsample divides by a number
btnGrossPay = tk.Button(tbMain, image=imgGrossPay) 



nbMain = ttk.Notebook(gui)

tabBob = ttk.Frame(nbMain)
lblBob = tk.Label(tabBob, text="Enter Bob's Hours")
txtBob = tk.Entry(tabBob)
nbMain.add(tabBob, text="Bob")

tabSally = ttk.Frame(nbMain)
lblSally = tk.Label(tabSally, text="Enter Sally's Hours")
txtSally = tk.Entry(tabSally)
nbMain.add(tabSally, text="Sally")

tabBecky = ttk.Frame(nbMain)
lblBecky = tk.Label(tabBecky, text="Enter Becky's Hours")
txtBecky = tk.Entry(tabBecky)
nbMain.add(tabBecky, text="Becky")

sbMain = tk.Frame(gui, border=3, relief="sunken")

lblStatus = tk.Label(sbMain, text="Status: ready....")






gui.config(menu=mnMain)
tbMain.pack(fill="both")
nbMain.pack(fill="both", expand=True)
sbMain.pack(fill="both")

btnGrossPay.grid(row=0, column=0, padx=5, pady=5)

lblBob.grid(row=0, column=0, padx=10, pady=45)
txtBob.grid(row=1, column=0, padx=10, pady=23)
lblSally.grid(row=0, column=0, padx=10, pady=45)
txtSally.grid(row=1, column=0, padx=10, pady=23)
lblBecky.grid(row=0, column=0, padx=10, pady=45)
txtBecky.grid(row=1, column=0, padx=10, pady=23)


lblStatus.grid(row=0, column=0)





#guard
if __name__=="__main__":
    gui.mainloop()
    



