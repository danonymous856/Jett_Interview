# Level-Order Traversal

## Algorithm

![](../../../../../Pictures/dsa in python/Screenshot 2022-07-17 131638.png)![](../../../../../Pictures/dsa in python/Screenshot 2022-07-17 131705.png)![](../../../../../Pictures/dsa in python/Screenshot 2022-07-17 131732.png)

To do a level order traversal of a binary tree we require **QUEUE** data structure.


![](../../../../../Pictures/dsa in python/Screenshot 2022-07-17 132130.png)![](../../../../../Pictures/dsa in python/Screenshot 2022-07-17 132151.png)![](../../../../../Pictures/dsa in python/Screenshot 2022-07-17 132217.png)![](../../../../../Pictures/dsa in python/Screenshot 2022-07-17 132251.png)![](../../../../../Pictures/dsa in python/Screenshot 2022-07-17 132310.png)![](../../../../../Pictures/dsa in python/Screenshot 2022-07-17 132330.png)![](../../../../../Pictures/dsa in python/Screenshot 2022-07-17 132352.png)

## Implementation

Now that you are familiar with the algorithm, let’s jump to the implementation in Python. First, we’ll need to implement Queue so that we can use its object in our solution of level-order traversal.
        
    look queue.py file

The constructor of the Queue class initializes self.items to an empty list on line 3. This list will store all the elements in the queue. We assume the last element to be the front of the queue and the first element to be the back of the queue.

To perform the enqueue operation, in the enqueue method, we make use of the insert method of Python list which will insert item on the 0th index in self.items as specified on line 6. On the other hand, in the dequeue method, we use the pop method of Python list to pop out the last element as the queue follows the First-In, First-Out property. The method also ensures that the pop method is only called if the queue is not empty. To see if a queue is empty or not, the is_empty method comes in handy which checks for the length of self.items and compares it with 0. If the length of self.items is 0, True is returned, otherwise, False is returned.

The peek method will return the value of the last element in self.items which we assume to be the front of our queue. We have also overridden the len method on line 19 which calls the size method on line 22. The size method returns the length of self.items.


    look level-order funtion.py file

In the code above, first of all, we handle an edge case on line 2, i.e., start (root node) is None or we have an empty tree. In such a case, we return from the levelorder_print method.
On line 5, we initialize a Queue object from the class we just implemented and name it as queue to which we enqueue start on line 6 as described in the algorithm.
traversal is initialized to an empty string on line 8. Next, we set up a while loop on line 9 which runs while the length of the queue is greater than 0. Just as depicted in the algorithm, we append an element using the peek method to traversal and also concatenate a - so that the traversal appears in a format where the visited nodes will be divided by -. Once traversal is updated to register the node we visit, we dequeue that node and save it in the variable node on line 11. From lines 13-16, we check for the left and the right children of node and enqueue them to queue if they exist.

Finally, *we return traversal on line 18 which will have all the nodes we visited according to level-order.*

In the code widget below, we have added levelorder_print to BinaryTree class and have also added "levelorder" as a traversal_type to print_tree method.

    visit level-order together.py