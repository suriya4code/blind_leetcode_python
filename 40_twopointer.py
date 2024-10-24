class Solution:
    # @param A : list of integers
    # @param B : integer
    # @return a list of integers
    def solve(self, A, B):
        # subarray with sum B
        x,y = 0, 0
        n = len(A)
        sum = 0
        while y < n:
            sum += A[y]
            if sum == B:
                return A[x:y+1]
            while sum > B:
                sum -= A[x]
                x += 1
                if sum == B:
                    return A[x:y+1]
            y += 1
        return -1


A = [1,2,3,4,5]
B = 5

print(Solution().solve(A,B))