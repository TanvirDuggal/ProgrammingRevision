# -*- coding: utf-8 -*-
"""
Created on Tue Dec  8 21:39:13 2020

@author: Tanvy
"""

class Node:
    def __init__(self, dt):
        self.left  = None
        self.dt    = dt
        self.right = None
        
class Tree:
    root = None
    def __init__(self):
        pass
    
    def add(self, dt):
        if self.root == None:
            self.root = Node(dt)
        else:
            self._add(Node(dt), self.root)
        
    def _add(self, node, root):
        if node.dt <= root.dt:
            if root.left != None:
                return self._add(node, root.left)
            else:
                root.left = node
        else:
            if root.right != None:
                return self._add(node, root.right)
            else:
                root.right = node
                
    def inOrder(self):
        self._inOrder(self.root)
    
    def _inOrder(self, root):
        if root:
            self._inOrder(root.left)
            print(root.dt)
            self._inOrder(root.right)
            
    def serialize(self):
        pass
    
    def _serialize(self, root):
        pass
            
          
def main():          
    dt = [27,14,35,10,19,31,42]

    tree = Tree()
    for i in dt:
        tree.add(i)

    tree.inOrder()
    
        
if __name__ == '__main__':
    main()