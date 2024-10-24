class Solution:
    # @param A : tuple of integers
    # @param B : integer
    # @return a list of integers
    def searchRange(self, A, B):
        n = len(A)
        from math import inf

        low, high = -inf, -inf

        for i in range(n):
            if A[i] == B:
                low = i
                break
        for i in range(n-1, -1, -1):
            if A[i] == B:
                high = i
                break
        return [low, high] if low != -inf and high != -inf else [-1, -1]



A = [1]
B = 1
print(Solution().searchRange(A, B)) # [3, 4]