# -*- coding: utf-8 -*-
"""
Created on Tue May 18 22:55:33 2021

@author: Tanvy
"""

def binarySearch(arr, numToSearch):
    if len(arr) == 1:
        if arr[0] == numToSearch:
            print("Found")
            return 1
        return 0
    
    if arr[len(arr)//2] == numToSearch:
        print("Found")
        return 1
    else:
        binarySearch(arr[:len(arr)//2], numToSearch)
        binarySearch(arr[len(arr)//2:], numToSearch)


arr = [3,5,6,7,88,123,567]
numToSearch = 888

binarySearch(arr, numToSearch)