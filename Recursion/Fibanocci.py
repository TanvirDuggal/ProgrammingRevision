# -*- coding: utf-8 -*-
"""
Created on Thu May 13 23:44:12 2021

@author: Tanvy
"""

def calFib_head(n):
    if n == 0:
        return 0
    
    if n == 1:
        return 1
    
    fib1 = calFib_head(n-1)
    fib2 = calFib_head(n-2)
    
    return fib1 + fib2


def calFib_tail(n, a=0, b=1):
    print(str(n) + " " + str(a) + " " + str(b))
    if n == 0:
        return a
    
    if n == 1:
        return b
    
    return calFib_tail(n-1,b, a+b)


n = 6
# print(calFib_head(n))
print(calFib_tail(n))