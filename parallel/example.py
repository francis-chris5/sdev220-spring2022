# -*- coding: utf-8 -*-
"""
Created on Tue May 17 17:56:20 2022

@author: Christopher S. Francis

@version: Python 3.10.2
"""

import multiprocessing as mp
import random


#print(mp.cpu_count())


def adding(arr):
    s = 0
    for a in arr:
        s += a
    return a

asyncResults = []
def collectResults(res):
    asyncResults.append(res)




if __name__ == "__main__":
    cores = mp.Pool(mp.cpu_count())
    
    data = []
    for i in range(24):
        data.append(random.random())
        
    
    
    
            ## synchronous parallel processing
            
    applyResult = cores.apply(adding, args=[data])
    
    print(applyResult)
    
    mapResult = cores.map(adding, [data])
    
    print(mapResult)
    
    
    
            ## asynchronous parallel processing
            

    cores.apply_async(adding, args=[data], callback=collectResults)
    
    ##could do lots of other things here while the function processes asynchronously
    
    cores.close() ##wait til cpu's are done
    cores.join() ##apply the results scattered around the various cores
    
    print(asyncResults)
    
    













    
    
    
    
    
    


















