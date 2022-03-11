#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Mar  8 18:10:57 2022

@author: Christopher S. Francis
@version: Python 3.9.2
"""


import tkinter as tk

class SalaryTab(tk.Frame):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.employee = None
        self.label = tk.Label(self, text="Salaried Employee")
        self.output = tk.Label(self, text="")
        
        self.label.grid(row=0, column=0, padx=10, pady=45)
        tk.Label(self, text="").grid(row=1, column=0, padx=10, pady=23)
        self.output.grid(row=2, column=0, padx=10, pady=18)
        
        
        
        
    def setEmployee(self, employee):
        self.employee = employee
        
    def getEmployee(self):
        return self.employee
        
    
    def setLabel(self, label):
        self.label["text"] = label
        
    
    def setOutput(self, output):
        self.output["text"] = output
        
        



class HourlyTab(SalaryTab):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.setLabel("Enter Hours worked")
        self.input = tk.Entry(self)
        
        self.input.grid(row=1, column=0, padx=10, pady=23)

    def getInput(self):
        return self.input




















#### white space