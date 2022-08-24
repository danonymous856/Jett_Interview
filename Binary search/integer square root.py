from random import random


def integer_square_root(k):
    start = 0
    end = k

    while end >= start:
        mid = (end + start) // 2
        mid_sq = mid * mid

        if mid_sq <= k:
            start = mid + 1
        elif mid_sq > k:
            end = mid - 1
    return start - 1


def find(A):
    low = 0
    high = len(A) - 1

    while low < high:
        mid = (low + high) // 2

        if A[mid] > A[high]:
            low = mid + 1
        elif A[mid] <= A[high]:
            high = mid

    return low


def CountAllPairs(N, K):
    count = 0
    if (N > K):

        # Initial count
        count = N - K
        for i in range(K + 1, N + 1):
            count = count + ((N - K) // i)

    return count

# A = [4, 5, 6, 7, 1, 2, 3]
# idx = find(A)
# print(A[idx])
print(CountAllPairs(7,5))