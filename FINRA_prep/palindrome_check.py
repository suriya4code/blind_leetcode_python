s = "marram"

def is_palindrome(s:str):
    n = len(s)
    l, r = 0, n-1
    while l<r:
        if s[l] != s[r]:
            return 0
        l+=1
        r-=1
    return 1


print(is_palindrome(s))

s = "A man, a plan, a canal: Panama"

def is_valid_palindrome_chars(s:str):
    char_str = [ i.lower() for i in s if i.isalpha()]
    n = len(char_str)
    l, r = 0, n-1
    while l<r:
        if char_str[l] != char_str[r]:
            return False
        l += 1
        r -= 1
    return True

print(is_valid_palindrome_chars(s))

# O(1) extra space: skip non-letters with the two pointers instead of building a new list
def is_valid_palindrome_chars_o1(s: str):
    l, r = 0, len(s) - 1
    while l < r:
        if not s[l].isalpha():
            l += 1
        elif not s[r].isalpha():
            r -= 1
        elif s[l].lower() != s[r].lower():
            return False
        else:
            l += 1
            r -= 1
    return True

print(is_valid_palindrome_chars_o1(s))
