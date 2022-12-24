def runningSum(n):
    temp = 0
    ans = []

    for i in n:
        temp += i
        ans.append(temp)

    return ans

print(runningSum([1,2,3,4,5,6,7]))