# -*- coding: utf-8 -*-
"""
Created on Tue May  3 18:28:31 2022

@author: Christopher S. Francis

@version: Python 3.10.2
"""



import threading

def busyWork(x):
    while x > 0:
        print(f"just doing some work, pass number {x}")
        x -= 1
        
        
def tediousStuff(y):
    while y > 12:
        print(f"carrying out some tedious tasks here number {y -12}")
        y -= 1
        

if __name__ == "__main__":
    
        ## remember the args must be an interable (set, list, tuple, dictionary...) 
        ## with MORE THAN 1 element
    firstThread = threading.Thread(target=busyWork, args=(10,))
    secondThread = threading.Thread(target=tediousStuff, args=(25,))
    
    firstThread.start()
    secondThread.start()
    
    firstThread.join()
    secondThread.join()
    
    print("----------  FINISHED NOW-------\n\n")
    
    