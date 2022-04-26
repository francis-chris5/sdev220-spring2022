# -*- coding: utf-8 -*-
"""
Created on Tue Apr 26 18:11:28 2022

@author: Christopher S. Francis

@version: Python 3.10.2
"""


from functools import wraps
import time
from tqdm import *
import psutil

# @todo make this function
def signature(func):
    @wraps(func)
    def wrapping(*args, **kwargs):
        sign = "Christopher S. Francis"
        date = "4/26/2022"
        print(f"this function was created by {sign} on {date}")
        return func(*args, **kwargs)#, f"this function was created by {sign}"
        
    return wrapping

def timed(func):
    @wraps(func)
    def wrapped(*args, **kwargs):
        start = time.time()
        beginning = psutil.Process().memory_info().rss / (1024 * 1024)
        res = func(*args, **kwargs)
        end = time.time()
        completing = psutil.Process().memory_info().rss / (1024 * 1024)
        print(f"that function took {end-start} seconds to run...")
        print(f"that seemed to take {completing - beginning} RAM...")
        return res
    return wrapped


@signature
def triple(x):
    threeTimes = x + x + x
    return threeTimes


@timed
def longFunction(x):
    factorial = 1
    for i in tqdm(range(x)):
        factorial *= (i+1)
        time.sleep(0.1)
    return factorial
        

print(triple(4))

print(longFunction(14))




















#####################################
        