# -*- coding: utf-8 -*-
"""
Created on Tue Apr 19 18:43:30 2022

@author: Christopher S. Francis

@version: Python 3.10.2
"""

stuff1 = [13, 1, 82, 7, 19, 54, 2, 4, 9, 3, 18, 11, 92, 44, 38]
stuff2 = [13, 1, 82, 7, 19, 54, 2, 4, 9, 3, 18, 11, 92, 44, 38]
stuff3 = [13, 1, 82, 7, 19, 54, 2, 4, 9, 3, 18, 11, 92, 44, 38]


stuff4 = "here is a collection of words that should work nicely to check out a sorting algorithm and compare it with others.".split(" ")
stuff5 =  "here is a collection of words that should work nicely to check out a sorting algorithm and compare it with others.".split(" ")
stuff6 = "here is a collection of words that should work nicely to check out a sorting algorithm and compare it with others.".split(" ")


def bubble(arr):
    bubbleSwapCounter = 0
    for i in range(0, len(arr) - 1):
        for j in range(i + 1, len(arr)):
            if arr[i] > arr[j]:
                temp = arr[i]
                arr[i] = arr[j]
                arr[j] = temp
                bubbleSwapCounter += 1
        #print(arr)
    print(f"number of bubble swaps {bubbleSwapCounter}")
    return arr


def insertion(arr):
    insertionSwapCounter = 0
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and key < arr[j]:
            arr[j+1] = arr[j]
            j -= 1
            insertionSwapCounter += 1
        arr[j+1] = key
        #print(arr)
    print(f"number of insertion swaps {insertionSwapCounter}")
    return arr


def selection(arr):
    selectionSwapCounter = 0
    for i in range(0, len(arr)):
        minIndex = i
        for j in range(i+1, len(arr)):
            if arr[j] < arr[minIndex]:
                minIndex = j
        temp = arr[i]
        arr[i] = arr[minIndex]
        arr[minIndex] = temp
        selectionSwapCounter += 1
    print(f"number of selection swaps {selectionSwapCounter}")
    return arr




if __name__=="__main__":
    print("Bubble: ")
    print(stuff1)
    print(bubble(stuff1))
    
    print("\n\n")
    
    print("insertion")
    print(stuff2)
    print(insertion(stuff2))
    
    print("\n\n")
    print(stuff3)
    print(selection(stuff3))
    
    
    print("\n\n*****************\n\n")
    
    print("Bubble: ")
    print(stuff4)
    print(bubble(stuff4))
    
    print("\n\n")
    
    print("insertion")
    print(stuff5)
    print(insertion(stuff5))
    
    print("\n\n")
    print(stuff6)
    print(selection(stuff6))
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    ###############################
    
    