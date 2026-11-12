class Solution:
    def solve(self, A, B, C):
        stack = [B]

        for i in range(A):
            if C[i] == 0:
                stack.pop()
            else:
                stack.append(C[i])
        return stack[-1]


A = 10
B = 23
C = [86, 63, 60, 0, 47, 0, 99, 9, 0, 0]
print(Solution().solve(A, B, C))