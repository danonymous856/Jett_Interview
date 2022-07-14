"""
Pre-order Traversal#
Here is the algorithm for a pre-order traversal:

Check if the current node is empty/null.
Display the data part of the root (or current node).
Traverse the left subtree by recursively calling the pre-order method.
Traverse the right subtree by recursively calling the pre-order method.
"""

def preorder_print(self,start,traversal):
    """root->left->right"""
    if start:
        traversal += (str(start.value) + "-")
        traversal = self.preorder_print(start.left, traversal)
        traversal = self.preorder_print(start.right, traversal)
    return traversal