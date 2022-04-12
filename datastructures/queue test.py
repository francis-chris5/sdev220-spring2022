# -*- coding: utf-8 -*-
"""
Created on Tue Apr 12 19:07:37 2022

@author: Christopher S. Francis

@version: Python 3.10.2
"""

import datastructures as ds
import numpy

print()
print()
print("queue")


queue = ds.Queue()

print(queue)

queue.poll(5)
queue.poll(12)
queue.poll(31)

print(queue)

print()

print(queue.remove())
print(queue.remove())

print(queue)

queue.poll(3)
queue.poll(8)

print()
print()

print(queue)


while queue.size() > 0:
    queue.poll(numpy.random.rand())
    queue.poll(numpy.random.rand())
    print(queue.remove())
    print(queue.remove())
    print(queue.remove())
    print(queue)




queue.poll(5)
queue.poll(12)
queue.poll(31)



queue.poll(3)
queue.poll(8)

print(queue)
while queue.size() > 0:
    if queue.peek() % 2 == 0:
        print(queue.remove())
    else:
        queue.remove()
