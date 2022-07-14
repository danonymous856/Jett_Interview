from stack.stack import Stack


def is_match(p1, p2):
    if p1 == "(" and p2 == ")":
        return True
    elif p1 == "{" and p2 == "}":
        return True
    elif p1 == "[" and p2 == "]":
        return True
    else:
        return False
    pass


def is_balanced(parameter):

    is_balanced = True
    index = 0
    s=Stack()

    while index < len(parameter) and is_balanced:
        paren = parameter[index]
        if paren in "({[":
            s.push(paren)
        else:
            if s.is_empty():
                is_balanced=False
                break
            else:
                top = s.pop()
                if not is_match(top,paren):
                    is_balanced = False
                    break
        index = index + 1

    if s.is_empty() and is_balanced:
        return  True
    else:
        return False




