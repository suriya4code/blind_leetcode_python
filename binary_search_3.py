class Solution:
    # @param A : tuple of integers
    # @param B : integer
    # @return an integer
    def search(self, A, B):
        n = len(A)
        low, high = 0, n-1
        while low <= high:
            mid = low + (high - low) // 2
            if A[mid] == B:
                return mid
            if A[low] <= A[mid]:
                if A[low] <= B <= A[mid]:
                    high = mid - 1
                else:
                    low = mid + 1
            else:
                if A[mid] <= B <= A[high]:
                    low = mid + 1
                else:
                    high = mid - 1
        return -1


A = [ 101, 103, 106, 109, 158, 164, 182, 187, 202, 205, 2, 3, 32, 57, 69, 74, 81, 99, 100 ]
B = 3
print(Solution().search(A, B))