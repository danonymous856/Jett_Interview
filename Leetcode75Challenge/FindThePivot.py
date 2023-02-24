def FindpivotSum(arr:list):
    leftsum =0
    for i in range(len(arr)):
        rightsum = sum(arr) - leftsum - arr[i]
        if rightsum == leftsum:
            return i
        leftsum+=arr[i]

print(FindpivotSum([1,7,3,6,5,6]))