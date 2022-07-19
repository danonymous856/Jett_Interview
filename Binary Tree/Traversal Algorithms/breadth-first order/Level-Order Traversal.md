# Level-Order Traversal

## Algorithm

![Screenshot 2022-07-17 131638](https://user-images.githubusercontent.com/81114860/179830329-e18215e5-0089-4238-9742-fe284a0d93f4.png)
![Screenshot 2022-07-17 131705](https://user-images.githubusercontent.com/81114860/179830363-5f934c41-f4e4-49d8-88f8-6f9b453035d3.png)
![Screenshot 2022-07-17 131732](https://user-images.githubusercontent.com/81114860/179830397-a5d01e18-6963-4df8-a1e7-70974ee20ed3.png)

To do a level order traversal of a binary tree we require **QUEUE** data structure.

![Screenshot 2022-07-17 132130](https://user-images.githubusercontent.com/81114860/179830588-a94c430d-8699-4170-a5d2-c41f0308e280.png)
![Screenshot 2022-07-17 132151](https://user-images.githubusercontent.com/81114860/179830599-ffda40fb-881b-4ac8-8591-9abeb3fed955.png)
![Screenshot 2022-07-17 132217](https://user-images.githubusercontent.com/81114860/179830624-e0b10ec1-c636-4cd6-8ce5-2bae2fe10c13.png)
![Screenshot 2022-07-17 132251](https://user-images.githubusercontent.com/81114860/179830636-3bf1894b-dbb6-4e8f-a71b-e864a4bed7a4.png)
![Screenshot 2022-07-17 132352](https://user-images.githubusercontent.com/81114860/179830677-ade26214-c406-4bea-92fe-e80dc7f4ea38.png)
![Screenshot 2022-07-17 132310](https://user-images.githubusercontent.com/81114860/179830647-141eaccf-a716-42e2-a6a7-0012ff759730.png)



## Implementation![Screenshot 2022-07-17 132330](https://user-images.githubusercontent.com/81114860/179830657-0389e86e-0ff3-481f-a47c-1cdbadb366af.png)


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
