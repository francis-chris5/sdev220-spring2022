# -*- coding: utf-8 -*-
"""
Created on Tue Feb 22 18:31:56 2022

@author: Christopher S. Francis

@version: Python 3.10.2
"""

import sys
sys.path.insert(0, "../pyOffice")


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
    empHours = [txtBob.get(), txtSally.get(), txtBecky.get()]
    empOutput = [lblBobOut, lblSallyOut, lblBeckyOut]
    for e in range(len(employees)):
        if not empHours[e].isnumeric():
            hours = 0
        else:
            hours = float( empHours[e])


        if isinstance(employees[e], Manager):
            hours = REGULAR_TIME
        if hours <= REGULAR_TIME:
            gross = hours * employees[e].getRate()
        else:
            gross = REGULAR_TIME * employees[e].getRate() + 1.5 * (hours - REGULAR_TIME) * employees[e].getRate()
        
        
        empOutput[e]["text"] = gross
        
    UpdateStatus(event, "updated everybody's gross pay...")


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
btnGrossPay.bind("<Button-1>", lambda event: GrossPay(event))



ioPrimary = tk.Frame(gui)

#tabBob = ttk.Frame(ioPrimary)
lblBob = tk.Label(ioPrimary, text="Enter Bob's Hours")
txtBob = tk.Entry(ioPrimary)
lblBobOut = tk.Label(ioPrimary, text="")


#tabSally = ttk.Frame(ioPrimary)
lblSally = tk.Label(ioPrimary, text="Enter Sally's Hours")
txtSally = tk.Entry(ioPrimary)
lblSallyOut = tk.Label(ioPrimary, text="")


#tabBecky = ttk.Frame(ioPrimary)
lblBecky = tk.Label(ioPrimary, text="Enter Becky's Hours")
txtBecky = tk.Entry(ioPrimary)
lblBeckyOut = tk.Label(ioPrimary, text="")



gui.bind("<Return>", lambda event: GrossPay(event))

## <"Control-Shift-H">  vs. <"Control-h">


sbMain = tk.Frame(gui, border=3, relief="sunken")

lblStatus = tk.Label(sbMain, text="Status: ready....")






gui.config(menu=mnMain)
tbMain.pack(fill="both")
ioPrimary.pack(fill="both", expand=True)
sbMain.pack(fill="both")

btnGrossPay.grid(row=0, column=0, padx=5, pady=5)

lblBob.grid(row=0, column=0, padx=10, pady=45)
txtBob.grid(row=1, column=0, padx=10, pady=23)
lblBobOut.grid(row=2, column=0, padx=10, pady=18)
lblSally.grid(row=0, column=1, padx=10, pady=45)
txtSally.grid(row=1, column=1, padx=10, pady=23)
lblSallyOut.grid(row=2, column=1, padx=10, pady=18)
lblBecky.grid(row=0, column=2, padx=10, pady=45)
txtBecky.grid(row=1, column=2, padx=10, pady=23)
lblBeckyOut.grid(row=2, column=2, padx=10, pady=18)


lblStatus.grid(row=0, column=0)





#guard
if __name__=="__main__":
    gui.mainloop()
    



