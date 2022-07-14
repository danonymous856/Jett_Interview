def reverse_string(string):
    """
    Python easy way of reversing a string
    :param : string
    :return: reverse string
    """
    return string[::-1]

print(reverse_string("malayalam"),reverse_string("donald"),reverse_string("zinda"))

from stack import Stack
def reverse_string_using_stack(stack, input_str):
    """
    using the Stack data structure to reverse the string
    :param stack: here we made stack pointing towards the Stack class
    :param input_str:
    :return:
    """
    for i in range(len(input_str)):
        stack.push(input_str[i])
    rev_str = ""
    while not stack.is_empty():
        rev_str += stack.pop()

    return rev_str

stack = Stack()
input_str = "nnelg"
print(reverse_string_using_stack(stack, input_str))