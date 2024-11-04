class Solution:
    # @param A : list of integers
    # @param B : integer
    # @return an integer
    def solve(self, A, B):
        A.sort()
        l=0
        r=1
        cnt=0
        while(r<len(A)):
            if abs(A[l]-A[r])==B:
                if l!=r:
                    cnt+=1
                    l+=1
                    r+=1
                while(l<len(A) and A[l]==A[l-1]):
                    l+=1
                while(r<len(A) and A[r]==A[r-1]):
                    r+=1
                if l==r:
                    r+=1
            elif abs(A[l]-A[r])<B:
                r+=1
            else:
                l+=1
            if l==r:
                r+=1
        return cnt




print(Solution().solve([1, 2, 3, 4, 5], 2)) # 3