# Calculating the Height of a Binary Tree

## Height of Tree

Let’s start by defining the height of a tree. The height of a tree is the height of its root node. Now let’s see what we mean by the height of a node:

## Height of Node

The height of a node is the number of edges on the longest path between that node and a leaf. The height of a leaf node is 0.

Recursively defined, the height of a node is one greater than the max of its right and left children’s height.

Below is an example of a binary tree labeled with heights of individual nodes:

![Screenshot 2022-07-21 234345](https://user-images.githubusercontent.com/81114860/180284731-912e40e2-1ab4-4a1c-81f1-81d4c6d3a24a.png)

## Algorithm

In this lesson, we will consider the recursive approach to calculate the height of a tree. The idea is to break down the problem using recursion and traverse through the left and right subtree of a node to calculate the height of that node. Once we get the height of the left and right subtree, we will consider the maximum of the two heights plus one to be the height of the tree.

## Implementation
Let’s move to the implementation in Python:

    look the .py file for height() function

In the code above, our base case is when node equals None. If node equals None, we return -1 on line 3 as we have gone past the leaf nodes. Once a leaf node discovers that its left and right children are reporting heights of -1 each, it will add 1 to -1 and return 0 as its height.
In lines 4-5, we recursively call the height method on the left child and the right child. The final height is calculated by adding 1 to the maximum height of the left and right subtree, as height is the longest path between that node and the leaf node. The final height is what is returned from the method.

Let’s run this code step by step in the illustration below:


I hope the visuals are helpful to understand the algorithm.

In the code widget, the height method is made part of the BinaryTree Class. Write your test cases to verify the height method. A sample test case has been given to you.



