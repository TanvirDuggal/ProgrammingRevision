# -*- coding: utf-8 -*-
"""
Created on Sat Nov 28 23:39:51 2020

@author: Tanvy
"""

class Node:
    def __init__(self, dt):
        self.next = None
        self.dt   = dt
        self.prev = None
        self.max  = None
        
class Stack:
    pointer = None
    maxVal  = None
    def __init__(self):
        pass
    
    def push(self, dt):
        if self.pointer == None:
            node         = Node(dt)
            self.pointer = node
            self.maxVal  = dt
            node.max     = dt
        else:
            node              = Node(dt)
            node.prev         = self.pointer
            self.pointer.next = node
            self.pointer      = node
            if self.maxVal < dt:
                self.maxVal = dt
                node.max    = dt
            else:
                node.max    = self.maxVal
    
    def pop(self):
        if self.pointer.prev == None:
            val          = self.pointer.dt
            self.pointer = None
            self.maxVal  = None
            return val
        else:
            val          = self.pointer.dt
            self.pointer = self.pointer.prev
            self.maxVal  = self.pointer.max
            return val
    
    def peek(self):
        return self.pointer.dt
    
    def getMax(self):
        return self.maxVal
    
    
def main():
    stack = Stack()
    stack.push(5)
    stack.push(4)
    stack.push(6)
    stack.push(3)
    stack.push(10)
    
    print(stack.maxVal)
    stack.pop()
    print(stack.maxVal)
    stack.pop()
    print(stack.maxVal)
    stack.pop()
    print(stack.maxVal)
    

if __name__ == '__main__':
    main()