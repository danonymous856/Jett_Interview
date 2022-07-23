"""
the main thing here is the function height but being a constructor we going to define every class and methods
"""

class Node(object):
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

class BinaryTree(object):
    def __init__(self,root):
        self.root = Node(root)

    def height(self,node):
        if node is None:
            return -1

        height_left = self.height(node.left)
        height_right = self.height(node.right)

        return 1 + max(height_right,height_left)

tree = BinaryTree(1)
tree.root.left = Node(2)
tree.root.right = Node(3)
tree.root.left.left = Node(4)
tree.root.left.right = Node(5)

print(tree.height(tree.root))
