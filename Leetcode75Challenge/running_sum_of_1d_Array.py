# def runningSum(n):
#     temp = 0
#     ans = []
#
#     for i in n:
#         temp += i
#         ans.append(temp)
#
#     return ans
#
# print(runningSum([1,2,3,4,5,6,7]))

def running(n :list):
    for i in range(1,len(n)):
        n[i] += n[i-1]

    return n

print(running([1,2,3,4]))