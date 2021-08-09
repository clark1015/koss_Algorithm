class Node:
    def __init__(self, key):
        self.key=key
        self.lchild=None
        self.rchild=None

class BinarySearchTree:
    def __init__(self):
        self.root=None
    def insert(self, key):
        if self.root == None:
            self.root = Node(key)
        else:
            current = self.root
            while True:
                if current.key > key:
                    if current.lchild == None:
                        current.lchild = Node(key)
                        break
                    