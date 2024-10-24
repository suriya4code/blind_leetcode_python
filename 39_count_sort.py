# count sort

class Solution:
    def solve(A):
        m = max(A)
        count = [0] * (m+1)
        
        for i in A:
            count[i] += 1
        res = []
        for j in range(len(count)):
            res.extend([j] * count[j])
        return res

print(Solution.solve([1, 2, 1, 3, 2, 1])) # [1, 1, 1, 2, 2, 3]