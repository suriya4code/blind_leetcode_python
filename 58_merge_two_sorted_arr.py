class Solution:
    def solve(A, B):
        n = len(A)
        m = len(B)
        i = 0
        j = 0
        res = []


        while i<n and j<m:

            if A[i] > B[j]:
                res.append(B[j])
                j += 1
            else:
                res.append(A[i])
                i += 1

        if i == n:
            res.extend(B[j:])
        if j == m:
            res.extend(A[i:])  

        return res
    
A = [4, 7, 9]
B = [2, 11, 19]

print(Solution.solve(A, B)) # [2, 4, 7, 9, 11, 19]