# -*- coding: utf-8 -*-
"""
Created on Tue May  4 22:50:18 2021

@author: Tanvy
"""
import sys

# Question: You are given n eggs and specified a number of k floors. 
# Write an algorithm to find the minimum number of drops is required to know the
# floor from which if the egg is dropped, it will break.

record = {}

def drop(eggs, floors):
    if eggs == 0 or floors == 0:
        return 0
    
    if eggs == 1:
        return floors
    
    if floors == 1 or floors == 0:
        return floors
    
    minn = sys.maxsize
    
    for i in range(1, floors+1):
        res = max(drop(eggs-1, i-1), 
                  drop(eggs, floors-i))
        
        if res < minn:
            minn = res
        
    return minn+1
    

def main():
    eggs   = 2
    floors = 10
    
    print(drop(eggs, floors))

if __name__ == '__main__':
    main()