# -*- coding: utf-8 -*-
"""
Created on Thu Dec 10 22:37:02 2020

@author: Tanvy
"""

class Node:
    def __init__(self, dt):
        self.left  = None
        self.dt    = dt
        self.right = None
        
class Tree:
    root = None
    
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
                
    def LCA(self, val1, val2):
        pass
                
def main():          
    dt = [27,14,35,10,19,31,42]

    tree = Tree()
    for i in dt:
        tree.add(i)

if __name__ == '__main__':
    main()
    