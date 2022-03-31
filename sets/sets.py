# -*- coding: utf-8 -*-
"""
Created on Thu Mar 31 19:13:36 2022

@author: Christopher S. Francis

@version: Python 3.10.2
"""



mySet = {1, 7, 18, 3}

for i in mySet:
    print(i)
    


A = {1, 2, 3, 4}
B = {2, 4, 6, 8}
C = {-1, 27, 38, "words", False}

print("\n\nIntersection:")
print(A.intersection(B))



print("\n\nUnion:")
print(A.union(B))


print("\n\ndifference")
print(A.difference(B))
print(B.difference(A))


print("\n\ndisjoint")
print(A.isdisjoint(B))
print(A.isdisjoint(C))

























#########################################
