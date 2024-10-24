class Solution:
        def findMedianSortedArrays(self, A, B):
            import math        
        
            if len(A)>len(B):
                A, B = B, A
            n1 = len(A)
            n2 = len(B)
            n=n1+n2
            l = 0
            h = n1
            while l <= h:
                cut1 = (l+h)//2
                cut2 = n//2 - cut1
                l1 = -math.inf if cut1==0 else A[cut1-1]
                l2 = -math.inf if cut2==0 else B[cut2-1]
                r1 = math.inf if cut1==n1 else A[cut1]
                r2 = math.inf if cut2==n2 else B[cut2]
                if l1>r2:h=cut1-1
                elif l2>r1:l=cut1+1
                else: return (max(l1, l2)+min(r1, r2))/2 if n%2==0 else min(r1, r2)
            return -1
A = [1, 4, 5]
B = [2, 3, 6]
print(Solution().findMedianSortedArrays(A, B)) # 3.5