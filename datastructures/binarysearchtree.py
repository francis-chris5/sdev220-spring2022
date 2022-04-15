# -*- coding: utf-8 -*-
"""
Created on Thu Apr 14 18:24:58 2022

@author: Christopher S. Francis

@version: Python 3.10.2
"""



class Node():
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None
        

def insert(root, key):
    ## if at beginning create the root
    if root == None:
        return Node(key)
    
    if key < root.key:
        root.left = insert(root.left, key)
    else:
        root.right = insert(root.right, key)
    
    return root


def inOrder(root):
    if root != None:
        ## left node right
        inOrder(root.left)
        print(" <<--  " + str(root.key) + "  -->>") ##do more interseting stuff than print here
        inOrder(root.right)
        


def preOrder(root):
    if root != None:
        ## node left right
        print(" <<--  " + str(root.key) + "  -->>") ##do more interseting stuff than print here
        preOrder(root.left)
        preOrder(root.right)



def postOrder(root):
    if root != None:
        ## left right node
        postOrder(root.left)
        postOrder(root.right)
        print(" <<--  " + str(root.key) + "  -->>") ##do more interseting stuff than print here
        

def search(root, key):
    print("...")
    if root == None:
        return False
    ## pre order node left right
    if root.key == key:
        return root.key
    elif key < root.key:
        return search(root.left, key)
    elif key > root.key:
        return search(root.right, key)
    
    
































####################################