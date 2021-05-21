# -*- coding: utf-8 -*-
"""
Created on Mon May 17 21:57:32 2021

@author: Tanvy
"""

def hanoi(disk, source, middle, destination):
    if disk == 0:
        print("No Disk Left")
        return
    
    hanoi(disk-1, source, destination, middle)
    print("Disk : " + str(disk) + " From " + source + " To " + destination)
    hanoi(disk-1, middle, source, destination)
    
hanoi(2, 'A', 'B', 'C')