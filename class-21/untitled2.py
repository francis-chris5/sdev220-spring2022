# -*- coding: utf-8 -*-
"""
Created on Tue Feb  1 19:09:53 2022

@author: c.s.francis
@version: Python 3.10.2
"""

import pyautogui as pyg
import time

# =============================================================================
# t = time.time()
# for i in range(121):
#     if (time.time() - t) > 0.001:
#         print("moving")
#         pyg.move(32, 32)
#         t = time.time()
#     print("running")
# =============================================================================
    

for i in range(10):
    pyg.move(23, 23)
    
pyg.click()

pyg.write("this is a keyboard now")










    
    




