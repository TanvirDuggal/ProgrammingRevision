# -*- coding: utf-8 -*-
"""
Created on Sun Nov 29 00:17:23 2020

@author: Tanvy
"""

class Node:
    def __init__(self, dt):
        self.prev = None
        self.dt   = dt
        self.next = None
        
class Stack:
    pointer = None
    def __init__(self):
        pass
    
    def push(self, dt):
        if self.pointer == None:
            self.pointer = Node(dt)
        else:
            node = Node(dt)
            node.prev         = self.pointer
            self.pointer.next = node
            self.pointer      = node
    
    def pop(self):
        if self.pointer.prev == None:
            val          = self.pointer.dt
            self.pointer = None
            return val
        else:
            val          = self.pointer.dt
            self.pointer = self.pointer.prev
            return val

def main():
    st    = "[{}]()([])"
    stack = Stack()
    dt    = True
    for i in st:
        if i == "[" or i == "(" or i == "{":
            stack.push(i)
        elif i == "]" or i == ")" or i == "}":
            if stack.pointer == None:
                dt = False
            else:
                stack.pop()
    
    if stack.pointer == None and dt == True:
        print("All Balanced")
    else:
        print("Not Balanced")
    
if __name__ == '__main__':
    main()