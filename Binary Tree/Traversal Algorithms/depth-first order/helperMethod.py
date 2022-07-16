"""
All the three traversal methods running by the Binary class requires
a helper method to invoke the tree traversal methods.
"""

class Node(object):
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

class BinaryTree(object):
    def __init__(self, root):
        self.root = Node(root)

    from post_order_traversal import postorder_print
    from pre_order_traversal import preorder_print
    from in_order_traversal import in_order_print

    def helper_print(self,traversal_type):
        if traversal_type == "preorder":
            return self.preorder_print(tree.root,"")
        elif traversal_type == "inorder":
            return self.in_order_print(tree.root,"")
        elif traversal_type == "postorder":
            return self.postorder_print(tree.root,"")

        else:
            print(f"traversal type {str(traversal_type)} is not supported")
            return False

tree = BinaryTree(1)
tree.root.left = Node(2)
tree.root.right = Node(3)
tree.root.left.left = Node(4)
tree.root.left.right = Node(5)
tree.root.right.left = Node(6)
tree.root.right.right = Node(7)

print(tree.helper_print("preorder"))
print(tree.helper_print("postorder"))
print(tree.helper_print("inorder"))

# 1-2-4-5-3-6-7-
# 4-2-5-1-6-3-7
# 4-5-2-6-7-3-1
#               1
#           /       \
#          2          3
#         /  \      /   \
#        4    5     6   7