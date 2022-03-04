# -*- coding: utf-8 -*-
"""
Created on Thu Mar  3 18:40:56 2022

@author: Christopher S. Francis

@version: Python 3.10.2
"""

import tkinter as tk


gui = tk.Tk()



#labels = []

# with open("list.txt", "r") as handler:
#     for line in handler:
#         if line.strip() != "":
#             labels.append(tk.Label(gui, text=line.strip()))


#       [ want ... loop ... filter] --keep it around
#       ( want ... loop ... filter) --grab as needed
labels = (tk.Label(gui, text=line.strip()) for line in open("list.txt", "r")  if line.strip() != "")



for l in labels:
    l.pack(padx=10, pady=20)





gui.mainloop()

