# -*- coding: utf-8 -*-
"""
Created on Thu Nov 19 00:05:29 2020

@author: Tanvy
"""

class Node:
    def __init__(self, dt):
        self.dt   = dt
        self.nxt  = None
        self.prev = None
        
class Stack:
    node    = ''
    pointer = ''
    def __init__(self):
        pass
    
    def push(self, dt):
        if self.node == '':
            self.node = Node(dt)
            self.pointer = self.node
        else:
            node             = Node(dt)
            self.pointer.nxt = node
            node.prev        = self.pointer
            self.pointer     = node
    
    def pop(self):
        res = self.pointer.dt
        self.pointer = self.pointer.prev
        if self.pointer == None:
            self.pointer = ''
            self.node    = '' 
        return res
    
    def peek(self):
        return self.pointer.dt

def main():
    postFix = "3 4 + 56 / 88 *"
    stack = Stack()
    
    for i in postFix.split(" "):
        if i not in ['+','-','/','*']:
            stack.push(i)
        else:
            firstNum  = stack.pop()
            secondNum = stack.pop()
            
            if i == "+":
                stack.push(float(firstNum) + float(secondNum))
            elif i == "-":
                stack.push(float(firstNum) - float(secondNum))
            elif i == "/":
                stack.push(float(firstNum) / float(secondNum))
            else:
                stack.push(float(firstNum) * float(secondNum))
                
    print(stack.peek())
    
    
if __name__ == '__main__':
    main()