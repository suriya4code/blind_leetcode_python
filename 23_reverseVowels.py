"""
Example 1:

Input: s = "hello"
Output: "holle"
Example 2:

Input: s = "leetcode"

"""

class Solution:
    def reverseVowels(self, s: str) -> str:
        l = len(s)
        idx = []
        word = ""
        for i in range(l):
            if s[i].lower() in "aeiou":
                idx.append(i)
                word += s[i]
        j = 0
        if len(word) == 0:
            return s
        word = word[::-1]
        res = ""
        for i in range(l):
            if j<len(word) and i == idx[j]:
                res+=word[j]
                j+=1
            else:
                res+=s[i]
        return res

            



s = "leetcode"
print(Solution().reverseVowels(s))