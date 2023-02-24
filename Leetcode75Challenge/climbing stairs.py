def climbStairs(n: int) -> int:
    first, second = 1, 1

    for i in range(n - 1):
        temp = first
        first = first + second
        second = temp

    return first

print(climbStairs(4))