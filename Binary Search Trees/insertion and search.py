class Node(object):
    def __int__(self,value):
        self.value = value
        self.left = None
        self.right = None

class BST(object):
    def __int__(self,root):
        self.root = Node(root)

    def search(self,target):
        self.serach_helper(self.root,target)

    def insertion(self,new_val):
        self.insert_helper(self.root, new_val)

    def insert_helper(self, start, new_val):
        if start.value < new_val:
            if start.right:
                self.insert_helper(start.right, new_val)
            else:
                start.right = Node(new_val)
        else:
            if start.left:
                self.insert_helper(start.left, new_val)
            else:
                start.left = Node(new_val)
        pass
    def serach_helper(self, current, target):
        if current:
            if current.value == target:
                return True
            elif current.value < target:
                return self.serach_helper(current.right, target)

            return self.serach_helper(current.left,target)
