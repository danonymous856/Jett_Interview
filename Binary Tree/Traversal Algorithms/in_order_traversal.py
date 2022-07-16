"""
in-order traversal is quite different from pre_order as ALogo implies :

check if the current node is empty or not.
traverse the left subtree recursively by the in-order method.
display the data part of the root .
traverse the right subtree of the node.

"""

def in_order_print(self,start,traversal):
    """left->root->right"""
    if start:
        traversal = self.in_order_print(start.left,traversal)
        traversal += (str(start.value) + "-")
        traversal = self.in_order_print(start.right,traversal)
    return traversal

"""
The inorder_print is pretty much the same as the preorder_print
 except that the order Root->Left->Right from pre-order changes
  to Left->Root->Right in in-order traversal. In order to achieve 
  this order, we just change the order of statements in the 
  if-condition, i.e., we first make a recursive call on the left child and after
   we are done with all the subsequent calls from line 4, we concatenate the value of the current
    node with traversal on line 5. Then, we can make a recursive call to
     right subtree on line 6. This will help us keep the
      order required for the in-order traversal.
"""