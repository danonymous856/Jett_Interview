def linear_search(arr,target):
    if len(arr) == 0:
        return -1
    for i in range(len(arr)-1):
        elements = arr[i]
        if elements == target:
            return i

def Binary_search(arr,target,start,end):
    if len(arr) == 0:
        return -1

    while start <= end:
        mid = (start+end)//2
        if target == arr[mid]:
            return
        elif target <= arr[mid]:
            return Binary_search(arr,target,start,mid-1)
        return Binary_search(arr,target,mid+1,end)

def swap(a,b):
    temp = a
    a = b
    b = temp
    return a,b

print(linear_search([1,2,4,5,6,7,8,9],5))

arr = [2,5,7,9,21,33,45,65,74]
print(Binary_search(arr, 33, 0, len(arr)-1))