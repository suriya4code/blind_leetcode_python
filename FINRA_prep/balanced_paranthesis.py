s = "{}[]"


def is_balanced(s:str):

    brackets = {"{":"}","[":"]","(":")"}
    stack = []
    for i in s:
        if i in brackets.keys():
            stack.append(i)
        else:
            if not stack: return False
            last = stack.pop()
            if i != brackets.get(last):
                return False
    return True

print(is_balanced(s))