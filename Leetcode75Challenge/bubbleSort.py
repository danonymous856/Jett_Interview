def bubbleSort(arr: list) -> list:
    for i in range(len(arr)):
        for j in range(1,len(arr)-i):
            if arr[j]<arr[j-1]:
                temp = arr[j]
                arr[j] = arr[j-1]
                arr[j-1] = temp
    return arr

a = [4,5,5,8,10,6,1,3,2]
print(bubbleSort(a))
