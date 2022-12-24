import random

class Node(object):
    def __init__(self,value):
        self.value = value
        self.right = None
        self.left = None

class BinaryTree(object):
    def __int__(self,root):
        self.root = Node(root)
    def BinarySearch(self,arr,start,end,target):
        """
        Recursive Binary Search
        """
        while start <= end:
            mid = (start+end)//2
            if target == arr[mid]:
                return  mid
            elif target <= arr[mid]:
                return self.BinarySearch(arr,start,mid-1,target)
            elif target > arr[mid]:
                return self.BinarySearch(arr,mid+1,end,target)
            return -1

array = []

for _ in range(10):
    array.append(input(f"enter the number:"))

print(array)

start = int(0)
end = int(len(array) - 1)
target = int(input("enter the number you want to find index for:"))

tree = BinaryTree()
print(tree.BinarySearch(array, start, end, target))





