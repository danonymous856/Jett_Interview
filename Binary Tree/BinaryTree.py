class Node(object):
    def __init__(self,value):
        self.value = value
        self.left = None
        self.right = None

class Binary_Tree(object):
    def __init__(self,root):
        self.root = Node(root) # Binary tree -> root -> node

tree = Binary_Tree(1)
tree.root.left = Node(2)
tree.root.right = Node(3)
tree.root.left.left = Node(4)
tree.root.left.right = Node(5)
tree.root.right.left = Node(6)
tree.root.right.right = Node(7)

"""
this makes the tree almost like this down below :
        1
      /    \ 
    2       3
  / |       |  \ 
 4  5       6   7       
"""

