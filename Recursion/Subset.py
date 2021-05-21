# -*- coding: utf-8 -*-
"""
Created on Thu May 20 22:33:17 2021

@author: Tanvy
"""

cont = []

def subset(arr, container="", index=0):
    if index == len(arr):
        cont.append(container)
        return container

    subset(arr, container + str(arr[index]), index+1)
    subset(arr, container, index+1)

arr = [1,2,3]
subset(arr)
print()
