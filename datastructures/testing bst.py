# -*- coding: utf-8 -*-
"""
Created on Thu Apr 14 18:50:02 2022

@author: Christopher S. Francis

@version: Python 3.10.2
"""


import binarysearchtree as bst

tree = bst.Node(3)
bst.insert(tree, 2)
bst.insert(tree, 21)
bst.insert(tree, 8)
bst.insert(tree, 1)
bst.insert(tree, 34)
bst.insert(tree, 7)
bst.insert(tree, 4)
bst.insert(tree, 16)


print("in order")
bst.inOrder(tree)

print("\n\npre order")
bst.preOrder(tree)

print("\n\npost order")
bst.postOrder(tree)


print("\n\nsearching...")
print(bst.search(tree, 34))
print(bst.search(tree, 17))














###############################