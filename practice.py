class Node:
    def __init__(self, item):
        self.data=item
        self.left=None
        self.right=None
    
    def size(self):
        if self.left:
            l=self.left.size()
        else:
            l=0
        if self.right:
            r=self.right.size()
        else:
            r=0
        return l+r+1
    
    def inorder(self):
        traversal=[]
        if self.left:
            traversal+=self.left.inorder()
        traversal.append(self.data)
        if self.right:
            traversal+=self.right.inorder()
        return traversal

class BinaryTree:
    def __init__(self, r):
        self.root = r
    
    def size(self):
        if self.root:
            return self.root.size()
        else:
            return 0

        
