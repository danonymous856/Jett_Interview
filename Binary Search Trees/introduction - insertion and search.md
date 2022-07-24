# Introduction - Insertion and Search

We will learn how to implement Binary Search Trees in Python and how to insert and search elements within them.

-> pics 
## Insertion

Let’s see how we can insert elements in a binary search tree. In the illustration below, we have an array of elements where we want to insert all the elements one by one into the binary search tree. The way we go about insertion is to start from the root node and compare the new value to be inserted with the current node’s value. If the new value is less than the value of the current node, then the new value must be inserted in the left subtree of the current node. On the other hand, if it’s greater, it must be inserted in the right subtree to satisfy the BST property. We keep comparing the values as we traverse the tree and insert wherever we find a null position.

## Insertion of a Reverse Sorted List

Let’s see what happens if we insert elements from a reverse sorted list one by one in a binary search tree.

-> pics

As you can see, we end up with a linear sort of a binary search tree. In such a case, if you want to find node 1 in the above binary search tree, you might have to traverse down. However, if you have a structure other than the linear one, then you can substantially cut down the number of operations that you would have to do to find node 1. We will look at that sort of a structure when we cover searching. The linear binary search tree is a structure we want to avoid when we perform operations on binary search trees because it kills the purpose of having a binary search tree. If you’re curious about how you can prevent getting the structure from reading data and forming a binary search tree out of it, then you can look into something called an AVL tree. An AVL tree rebalances the nodes so that you get a hierarchically spread-out structure instead of a linear one. However, that is beyond the scope of this lesson.

## Search

We search using a similar approach as we used in the insertion in a binary search tree. Starting from the root node, we decide which subtree to traverse by comparing the value to be searched with the current node. Then we traverse to the appropriate subtree and discard the other subtree that does not contain the element we are searching for due to the BST property.

-> pics

Now let’s also illustrate an example to search on a linear binary tree.

-> pics

As you can see from the illustration above, we don’t discard anything in a linear structure, so we have to traverse all the nodes to find the node we are looking for. This makes it an operation of O(n)
O(n)
 in the worst case. If we have a non-linear structure for a BST, the time complexity significantly improves to O(log n)
O(logn).

This table summarizes the time complexities for a BST:

-> pics

## Implementation

The implementation of the BST class is similar to the implementation of the BinaryTree class. The Node class is exactly the same as the Node class in the Binary Trees chapter.
Have a look at the implementation below:

## insert
Now we’ll look into the implementation of insert operation in Python.
The insert method on line 1 invokes the helper function (insert_helper) on line 2, while also passing self.root and new_val into that method. In the insert_helper method, we have current and new_val which refer to the current node and the new value to be inserted. In order to find the appropriate location to insert new_value, we compare current.data to new_value. If current.data is less than new_val, then new_val must be placed somewhere in the right subtree. Therefore, we check on line 6 if current.right is None. If it’s not, this implies that we have to traverse the tree further and we recursively call insert_helper on line 7 and pass current.right and new_value to it. On the other hand, if current.right is None, then current must be a leaf node, and we have found an appropriate position to insert the new_val. Then we initialize current.right to a new Node by passing new_val to the constructor on line 9.
Let’s talk about when current.data is greater than or equal to new_val. If that’s the case, we repeat what we discussed above about the code in lines 6-9, but replace current.right with current.left as new_val must be placed in the left subtree of the current node.

## search
Let’s discuss the search method:
If you get the hang of the insert operation, then the search method is relatively simple to understand. Like the insert method, the search method invokes a helper function (search_helper) and passes the root node and the value to search (find_val) to the helper method. It also returns whatever is returned from the helper method.

In search_helper, we check on line 5 if current is None. If it’s not, then the execution jumps to line 6 where the condition acts as a sort of base case to the recursive method. If the value of the current node (current.data) is equal to find_val, then we have found the node that we are supposed to search. True is returned on line 7 to send a confirmation back to the caller method. However, if the condition on line 6 does not evaluate to True, we check on line 8 to see if current.data is less than find_val. If this evaluates to True, find_val must be in the right subtree of the current node to which we make a recursive call on line 9. Otherwise, if current.data is greater than find_val, we make a recursive call to the left subtree on line 11.

The entire code that we have implemented can be found below. Make a BST and insert elements to it to verify the insert and the search methods.
