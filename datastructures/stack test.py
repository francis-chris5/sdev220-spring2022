# -*- coding: utf-8 -*-
"""
Created on Tue Apr 12 18:15:58 2022

@author: Christopher S. Francis

@version: Python 3.10.2
"""

import datastructures as ds
import numpy

print()
print()
print("Stack")


stack = ds.Stack()

print(stack)

stack.push(5)
stack.push(12)
stack.push(31)

print(stack)

print()

print(stack.pop())
print(stack.pop())

print(stack)

stack.push(3)
stack.push(8)

print()
print()

print(stack)


while stack.size() > 0:
    stack.push(numpy.random.rand())
    stack.push(numpy.random.rand())
    print(stack.pop())
    print(stack.pop())
    print(stack.pop())
    print(stack)




stack.push(5)
stack.push(12)
stack.push(31)



stack.push(3)
stack.push(8)

print(stack)
while stack.size() > 0:
    if stack.peek() % 2 == 0:
        print(stack.pop())
    else:
        stack.pop()













########################################