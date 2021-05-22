# -*- coding: utf-8 -*-
"""
Created on Sat May 22 00:04:41 2021

@author: Tanvy
"""

def _superDigit(N, value=0):
    if len(N) == 0:
        if len(str(value)) > 1:
            return _superDigit(str(value), 0)
        else:
            return value
        return value
    
    value = _superDigit(N[1:], value+int(N[0]))
    return value

def repeatValueOfN(n, k):
    value = 0
    
    for index in str(n):
        value += int(index) * k
        
    return str(value)

if __name__ == '__main__':
    n = 4757362
    k = 10000
    
    # print(repeatValueOfN(n, k))
    
    print(_superDigit(repeatValueOfN(n, k)))
    