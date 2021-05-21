# -*- coding: utf-8 -*-
"""
Created on Mon May 17 23:16:58 2021

@author: Tanvy
"""

def search(arr, num):
    if len(arr) == 0:
        print("Not Found")
        return
        
    if arr[0] == num:
        print("Found")
        return
        
    search(arr[1:], num)


def searchWithIndex(arr, num, currentIndex = 0):
    if currentIndex == len(arr):
        print("Not Found")
        return
    
    if len(arr) == 0:
        print("Empty Array")
        return
    
    if arr[currentIndex] == num:
        print("Number " + str(num) + " Found at Index : " + str(currentIndex))
        return
    
    searchWithIndex(arr, num, currentIndex+1)  
    
arr = [3,6,89,12,34,0,56]
num = 0

searchWithIndex(arr, num)