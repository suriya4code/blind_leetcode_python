from collections import Counter

s = "ssaadfgsa"

def keep_only_repeating(s:str):
    
    res = []

    count = Counter(s)

    for i in s:
        if count.get(i) > 1 and i not in res:
            res.append(i)
    return "".join(res)



def keep_only_repeating_dict(s:str):

    char_dict = {}
    res = []

    for i in s:
        if i in char_dict and i not in res:
            res.append(i)

        char_dict[i] = 1

    return "".join(res)

def keep_repeating_with_count(s:str):
    char_count = {}

    for i in s:
        char_count[i] = char_count.get(i, 0) + 1

    return {i: char_count[i] for i in char_count if char_count[i] > 1}

print(keep_only_repeating(s))
print(keep_only_repeating_dict(s))
print(keep_repeating_with_count(s))