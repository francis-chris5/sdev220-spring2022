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
from tabs import *


# employees = [
#     Laborer(name="Bob", rate=17.34, vacationDays = "july 4", department="labor"),
#     Clerical(name ="Sally", rate = 19.87, vacationDays = "whenever", access="VIP"),
#     UpperMgmt(name="Becky", salary = 43210, bonus="20% of new sales"),
#     MiddleMgmt(name="David", salary=36222),
#     Clerical(name="Diane", rate=19.87, vacationDays="whenever", access="VIP")
#     ]
employees = []

tabs = []

REGULAR_TIME = 40

def AddEmployee(Event):
    dlgAddEmployee = tk.Toplevel(gui)

    empType = tk.StringVar()
    empType.set("Laborer")
    rdLaborer = tk.Radiobutton(dlgAddEmployee, text="Laborer", value="Laborer", variable=empType)
    rdClerical = tk.Radiobutton(dlgAddEmployee, text="Clerical", value="Clerical", variable=empType)
    rdMidMgmt = tk.Radiobutton(dlgAddEmployee, text="MiddleMgmt", value="MiddleMgmt", variable=empType)
    rdUpMgmt = tk.Radiobutton(dlgAddEmployee, text="UpperMgmt", value="UpperMgmt", variable=empType)
    
    lblName = tk.Label(dlgAddEmployee, text="Name:")
    txtName = tk.Entry(dlgAddEmployee)
    lblRate = tk.Label(dlgAddEmployee, text="Rate/Salary:")
    txtRate = tk.Entry(dlgAddEmployee)
    btnAddEmployee = tk.Button(dlgAddEmployee, text="Add Employee")
    btnAddEmployee.bind("<Button-1>", lambda event: includeEmployee(event, empType, txtName, txtRate))
    
    rdLaborer.grid(row=0, column=0, padx=15, pady=10)
    rdClerical.grid(row=1, column=0, padx=15, pady=10)
    rdMidMgmt.grid(row=2, column=0, padx=15, pady=10)
    rdUpMgmt.grid(row=3, column=0, padx=15, pady=10)
    lblName.grid(row=0, column=1, padx=15, pady=10)
    txtName.grid(row=0, column=2, padx=15, pady=10)
    lblRate.grid(row=1, column=1, padx=15, pady=10)
    txtRate.grid(row=1, column=2, padx=15, pady=10)
    btnAddEmployee.grid(row=1, column=3, pady=30, padx=30)



def includeEmployee(event, empType, empName, empRate):
    employee = Employee(name="Error", rate=0)
    if empRate.get() == "" or empRate.get() == None:
        rate = 0
    else:
        rate = float(empRate.get())
    match empType.get():
        case "Laborer":
            employee = Laborer(name=empName.get(), rate=rate, vacationDays=None, department=None)
        case "Clerical":
            employee = Clerical(name=empName.get(), rate=rate, vacationDays=None, access=None)
        case "MiddleMgmt":
            employee = MiddleMgmt(name=empName.get(), salary=rate)
        case "UpperMgmt":
            employee = UpperMgmt(name=empName.get(), salary=rate, bonus="")
        case __:
            pass
            
            
    employees.append(employee)
    AddTab(None, employee)
    empName.delete(0, tk.END)
    empRate.delete(0, tk.END)
    empName.focus()




def AddTab(event, employee):
    if isinstance(employee, Manager):
        tabEmployee = SalaryTab(nbMain)
    else:
        tabEmployee = HourlyTab(nbMain)
    tabEmployee.setEmployee(employee)
    nbMain.add(tabEmployee, text=tabEmployee.getEmployee().getName())
    tabs.append(tabEmployee)


def GrossPay(event):
    for e in range(len(employees)):
        if not isinstance(employees[e], Manager):
            if not tabs[e].getInput().get().isnumeric():
                hours = 0
            else:
                hours = float( tabs[e].getInput().get())


        if isinstance(employees[e], Manager):
            hours = REGULAR_TIME
        if hours <= REGULAR_TIME:
            gross = hours * employees[e].getRate()
        else:
            gross = REGULAR_TIME * employees[e].getRate() + 1.5 * (hours - REGULAR_TIME) * employees[e].getRate()
        
        
        tabs[e].setOutput(gross)


def UpdateStatus(event, status):
    lblStatus["text"] = "Status: " + status





gui = tk.Tk()
gui.geometry("765x432")
gui.title("Payroll Thing")



mnMain = tk.Menu(gui)
mnFile = tk.Menu(mnMain, tearoff=0)
mnFile.add_command(label="New Employtee", command=lambda: AddEmployee(None))
mnMain.add_cascade(label="File", menu=mnFile)
mnPay = tk.Menu(mnMain, tearoff=0)
mnPay.add_command(label="Gross Pay", command= lambda : GrossPay(None))
mnMain.add_cascade(label="Payroll", menu=mnPay)


tbMain = tk.Frame(gui, border=3, relief="groove")
imgGrossPay = tk.PhotoImage(file="gross.png")
imgGrossPay = imgGrossPay.subsample(2) ##subsample divides by a number
btnGrossPay = tk.Button(tbMain, image=imgGrossPay)
btnGrossPay.bind("<Button-1>", lambda event: GrossPay(event))


nbMain = ttk.Notebook(gui)

for e in employees:
    AddTab(None, e)
    

gui.bind("<Return>", lambda event: GrossPay(event))

## <"Control-Shift-H">  vs. <"Control-h">


sbMain = tk.Frame(gui, border=3, relief="sunken")

lblStatus = tk.Label(sbMain, text="Status: ready....")






gui.config(menu=mnMain)
tbMain.pack(fill="both")
nbMain.pack(fill="both", expand=True)
sbMain.pack(fill="both")

btnGrossPay.grid(row=0, column=0, padx=5, pady=5)



lblStatus.grid(row=0, column=0)





#guard
if __name__=="__main__":
    gui.mainloop()
    



