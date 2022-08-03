class Node(object):
    def __init__(self,value):
        self.value = value
        self.right = None
        self.left = None

class BinaryTree(object):
    def __int__(self,root):
        self.root = Node(root)

    def BinarySearch(self,arr,start,end,mid,target):
        """
        Recursive Binary Search
        """
        if target == arr[mid]:
            return  mid
        elif target <= arr[mid]:
            return self.BinarySearch(arr,start,mid-1,mid,target)

        return self.BinarySearch(arr,mid+1,end,mid,target)