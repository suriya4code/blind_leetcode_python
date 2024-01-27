class Solution:
    # @param A : tuple of integers
    # @return a strings
    
    def largestNumber(self, A:list):
        from functools import cmp_to_key
        A = [str(i) for i in A]
        A.sort(key=cmp_to_key(self.compare_num))
        return int("".join(A))
    
    def compare_num(self,x,y):
        if int(x+y) > int(y+x):
            return -1
        return 1


A = [2, 3, 9, 0]
A = [0,0,0,0]
# A = [8,89]
print(Solution().largestNumber(A))