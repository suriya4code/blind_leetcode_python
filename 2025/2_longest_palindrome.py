class Solution:

    def solve(s):
        n = len(s)
        start = 0
        cnt = 0
        res = []
        
        for i in range(n):
            sub_str = s[start:i]
            if sub_str == sub_str[::-1]:
                cnt += 1
                res.append(sub_str)
        return max(res, key=len)
    
    def solve2(s):
        n = len(s)
        start = 0
        end = 0
        res = []

        for i in range(n):
            for j in range(i, n):
                sub_str = s[i:j+1]
                if sub_str == sub_str[::-1]:
                    res.append(sub_str)
        return max(res, key=len)

        
                



s = "cbbd"
print(Solution.solve2(s))