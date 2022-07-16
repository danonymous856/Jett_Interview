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

"""
if we check start(which is the current node) is empty or not .
If not then we append start.value to the traversal string and recursively call
preorder_print on start.left and start.right which are the right and left child of the current node.
Finally, we will return the traversal in case start is not None .
--- Traversal is a string that concatinates the value of nodes in an order we visit them. --- 
"""
