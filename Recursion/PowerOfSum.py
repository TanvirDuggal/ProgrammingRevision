# -*- coding: utf-8 -*-
"""
Created on Thu May 20 00:08:12 2021

@author: Tanvy
"""

import math

def _powerSum(X, N, powerContainer, index=0, container = "", counter=0):
    if index == len(powerContainer):
        addedValues = 0
        for objectValue in container.split(" "):
            if objectValue != '':
                addedValues += math.pow(int(objectValue),N)
        
        if addedValues == X:
            counter += 1
        return counter
    
    counter = _powerSum(X, N, powerContainer, index+1, container+" " +str(powerContainer[index]), counter)
    counter = _powerSum(X, N, powerContainer, index+1, container, counter)
    
    return counter


def checkLimitOfPower(X, N):
    container = []
    for index in range(1, X+1):
        if math.pow(index, N) <= X:
            container.append(index)
            
    return container

def powerSum(X, N):
    return _powerSum(X, N, checkLimitOfPower(X, N))
    
    
if __name__ == '__main__':
    X = 1000
    N = 2
    print(powerSum(X, N))