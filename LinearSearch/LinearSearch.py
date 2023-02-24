def linear(arr: list, target:int)->int:
    for i in range(len(arr)):
        if arr[i]==target:
            return i

print(linear([1,2,3,4,5,6,45],4))
        