# Reverse Level-Order Traversal

we will go over how to perform a reverse level-order traversal in a binary tree. We then code a solution in Python building on our binary tree class.

-> pics

## Algo

To solve this problem, we’ll use a queue again just like we did with level-order traversal, but with a slight tweak; **we’ll enqueue the right child before the left child**.
Additionally, we will use a **stack**.
The algorithm starts with enqueuing the root node. As we traverse the tree, we dequeue the nodes from the queue and push them to the stack. After we push a node on to the stack, we check for its children, and if they are present, we enqueue them. This process is repeated until the queue becomes empty. In the end, popping the element from the stack will give us the reverse-order traversal.

->pics

## Implementation

Now that we have studied the algorithm, let’s jump to the implementation in Python. First, we’ll implement Stack class:

    look reverse-levelorder traversal.py ln:1 - 29

In the constructor, we initialize self.items to an empty list just like we did with Queue. In the push method on line 11, the built-in append method is used to insert elements (item) to self.items. So whenever we push an element onto the stack, we append that element to self.items. The pop method on line 14 first checks whether the stack is empty or not using the is_empty method implemented on line 22. In the pop method, we use pop method of Python list to pop out the last element as the stack follows the First-In, Last-Out property and the latest element we inserted is at the end of self.items. The is_empty method on line 22 checks for the length of self.items by comparing it with 0 and returns the boolean value accordingly. On line 18, peek method is implemented which may or may not be used in the solution of our lesson problem. If the stack is not empty, the last element of self.items is returned on line 20.
The size and len method have also been added in a way as to the Queue class. Also, we have an str method on line 25 which iterates through self.items and concatenates them into a string which is returned from the method.

    look reverse-levelorder traversal.py ln:31 - 53

In the code above, we handle an edge case on line 2, i.e., the start (root node) is None or we would have an empty tree. In such a case, we return from the reverse_levelorder_print method.

On line 5 and line 6, we initialize a Queue object and a Stack object from the class we just implemented. In the next line, we enqueue start to queue as described in the algorithm. traversal is initialized to an empty string on line 10. Next, we set up a while loop on line 11 which runs until the length of the queue is greater than 0. Just as depicted in the algorithm, we dequeue an element from the queue and push it on the stack on line 12. From lines 16-19, we check for the right and left children of the node and enqueue them to queue if they exist. At the end of the while loop, stack will contain all the nodes of the tree. On line 21, we are using a while loop to pop elements from the stack and concatenate them to traversal which is returned from the method on line 25.

In the code widget below, we have added reverse_levelorder_print to the BinaryTree class and have also added "reverse_levelorder" as a traversal_type to print_tree method.

    look reverse-levelorder traversal.py ln:56 - 150(includes reverse_levelorder_print function; ln:126-150)



