s = "foo bar"


def reverse_in_place(s:str):
    lst = s.split(" ")
    return " ".join((i[::-1] for i in lst))

print(reverse_in_place(s))


def reverse_in_place_On(s:str):
    result = ""
    tmp = ""
    for i in s:
        if i == " ":
            result += tmp[::-1]
            result += " "
            tmp = ""
            continue
        tmp += i
    if tmp:
        result += tmp[::-1]
    return result


print(reverse_in_place_On(s))

