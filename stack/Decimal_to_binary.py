from stack import Stack
def decimalToBinary(n):
    if n == 0:
        return 0

    s = Stack()

    while n > 0:
        rem = n%2
        s.push(rem)
        n = n//2

    bin = ""

    while not s.is_empty():
        bin += str(s.pop())

    return bin

print(decimalToBinary(242))