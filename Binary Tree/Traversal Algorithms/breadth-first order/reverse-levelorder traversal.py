class Stack(object):
    def __init__(self):
        self.items = []

    def __len__(self):
        return self.size()

    def __str__(self):
        s = ""
        for i in range(len(self.items)):
            s+=str(self.items[i].value)
        return  s

    def push(self,item):
        self.items.append(item)

    def pop(self):
        if not self.is_empty():
            return self.items.pop()

    def is_empty(self):
        return  len(self.items) == 0

    def peek(self):
        if not self.is_empty():
            return self.items[-1]

    def get_stack(self):
        return self.items

    def size(self):
        return len(self.items)
        pass

class Queue(object):
    def __init__(self):
        self.items = []

    def enqueue(self,item):
        self.items.insert(0,item)

    def dequeue(self):
        if not self.is_empty():
            return self.items.pop()

    def is_empty(self):
        return len(self.items) == 0
        pass

    def peek(self):
        if not self.is_empty():
            return self.items[-1].value

    def __len__(self):
        return self.size()

    def size(self):
        return len(self.items)
        pass

class Node(object):
    def __init__(self,value):
        self.value = value
        self.left = None
        self.right = None

class BinaryTree(object):
    def __init__(self,root):
        self.root = Node(root)

    def print_tree(self,traversal_type):
        if traversal_type == "preorder":
            return self.preorder_print(tree.root,"")
        elif traversal_type == "inorder":
            return self.inorder_print(tree.root,"")
        elif traversal_type == "postorder":
            return self.postorder_print(tree.root,"")
        elif traversal_type == "levelorder":
            return self.levelorder_print(tree.root)
        elif traversal_type  == "reverse_levelorder":
            return self.reverse_print(tree.root)

        else:
            return f"there is no traversal type like {str(traversal_type)}"

    def preorder_print(self, start, traversal):
        if start:
            traversal += (str(start.value) + "-")
            traversal = self.preorder_print(self.left, "-")
            traversal = self.preorder_print(self.righ, "-")
        return  traversal

    def inorder_print(self,start,traversal):
        if start:
            traversal = self.inorder_print(self.left,"-")
            traversal += (str(start.value)+"-")
            traversal = self.inorder_print(self.right,"-")
        return  traversal

    def postorder_print(self,start,traversal):
        if start:
            traversal = self.postorder_print(self.left,"-")
            traversal = self.postorder_print(self.right,"-")
            traversal += (str(start.value) + "-")
        return traversal

    def levelorder_print(self,start):
        if start is None:
            return

        queue = Queue()
        queue.enqueue(start)

        traversal = ""
        while len(queue) > 0:
            traversal += str(queue.peek()) + "-"
            node = queue.dequeue()

            if node.left:
                queue.enqueue(node.left)
            if node.right:
                queue.enqueue(node.right)
        return traversal

    def reverse_print(self,start):
        if start is None:
            return

        queue = Queue()
        stack = Stack()
        queue.enqueue(start)

        traversal = ""
        while len(queue) > 0:
            node = queue.dequeue()

            stack.push(node)

            if node.right:
                queue.enqueue(node.right)
            if node.left:
                queue.enqueue(node.left)

        while len(stack) > 0:
            node = stack.pop()
            traversal += str(node.value) + "-"

        return traversal

tree = BinaryTree(1)
tree.root.left = Node(2)
tree.root.right = Node(3)
tree.root.left.left = Node(4)
tree.root.left.right = Node(5)

print(tree.print_tree("reverse_levelorder"))



