"""
Input: s = "3[a]2[bc]"
Output: "aaabcbc"

Input: s = "3[a2[c]]"
Output: "accaccacc"
"""

def decodeString(s:str):
    i = len(s)-1
    res = []
    word = ""
    while i>-1:
        if s[i] == "[":
            pass
        elif s[i] == "]":
            if word != "":
                res.insert(0,word)
            word = ""
        elif s[i].isnumeric():
            for j in range(int(s[i])):
                res.insert(0,word)
            word = ""
        else:
            word = s[i] + word
        i -= 1
    return "".join(res)


def decodeString2(s):
        stack=[]
        for c in s:
            if c!=']':
                stack.append(c)
            else:
                res=''
                while stack[-1]!='[':
                    res+=stack.pop()
                stack.pop()
                n=''
                while len(stack)!=0 and stack[-1].isdigit()==True:
                    n+=stack.pop()
                stack.append(res*int(n[::-1]))

        return ''.join([word[::-1] for word in stack])

s = "3[a]2[bc]"
# s = "2[abc]3[cd]ef"
s = "3[a2[c]]"
print(decodeString2(s))