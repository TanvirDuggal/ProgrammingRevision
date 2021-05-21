# -*- coding: utf-8 -*-
"""
Created on Tue May 11 22:17:37 2021

@author: Tanvy
"""

def headRecurrsion(n):
    if n == 0:
        return 1
    
    result1 = headRecurrsion(n-1)
    return n * result1

def tailRecurrsion(n, acc = 1):
    if n == 1:
        return acc
    
    return tailRecurrsion(n-1, n * acc)

print(tailRecurrsion(5))