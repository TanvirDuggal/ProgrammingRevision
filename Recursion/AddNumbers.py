# -*- coding: utf-8 -*-
"""
Created on Sun May  9 23:55:28 2021

@author: Tanvy
"""

def numberAdd(n):
    print(n)
    if n == 1:
        print("OUT")
        return 1
    print(">>> " + str(n + numberAdd(n-1)))
    return n + numberAdd(n-1)


print(numberAdd(3))