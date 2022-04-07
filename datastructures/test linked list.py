# -*- coding: utf-8 -*-
"""
Created on Thu Apr  7 19:09:49 2022

@author: Christopher S. Francis

@version: Python 3.10.2
"""

import datastructures as ds

five = ds.LLNode(5)
three = ds.LLNode(3)
seventeen = ds.LLNode(17)


five.next = three
three.next = seventeen

current = five
while current != None:
    print(current)
    current = current.next
    
print()
print()
print("add a node")

twelve = ds.LLNode(12)
three.next = twelve
twelve.next = seventeen

current = five
while current != None:
    print(current)
    current = current.next
    
    
print("\n\n")
print("different start")
current = three
while current != None:
    print(current)
    current = current.next
    



print("\n\ndelete a node")
five.next = twelve

current = five
while current != None:
    print(current)
    current = current.next


print()
print()
print()
print("Custom Class Linked List Combination")

boss = ds.Crew("Sally", "Manager", 45.67)
secretary = ds.Crew("Becky", "Administrative Assistanct", 22.34)
laborer1 = ds.Crew("Bob", "laborer", 17.34)
laborer2 = ds.Crew("David", "Laborer", 17.34)


boss.next = secretary
secretary.next = laborer1
laborer1.next = laborer2


current = boss
while current != None:
    print(current)
    current = current.next
    

























################################
    
