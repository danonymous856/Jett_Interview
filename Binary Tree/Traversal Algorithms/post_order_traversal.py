"""
ALGO:

check if root is empty/null
traverse to left subtree recursively on the method
traverse to right subtree recursively on the method
display the current root
"""
def postorder_print(self,start,traversal):
    """left->right->root"""
    if start:
        traversal = self.postorder_print(start.left,traversal)
        traversal = self.postorder_print(start.right,traversal)
        traversal += (str(start.value)+"-")
    return traversal
