


def TOH(N, src, temp, dest):
    if N == 0:
        return
    TOH(N-1, src, dest, temp)
    print([N,src, dest], end=' ')
    TOH(N-1, temp, src, dest)

TOH(3, 1, 2, 3)

class Solution:
    # @param A : integer
    # @return a list of list of integers
    def towerOfHanoi(self, A,source=1,destination=3,middle=2):
        return self.towerOfHanoi(A-1,source,middle,destination)+[[A,source,destination]]+self.towerOfHanoi(A-1,middle,destination,source) if A else []
    
Solution().towerOfHanoi(3) # [[1, 1, 3], [2, 1, 2], [1, 3, 2], [3, 1, 3], [1, 2, 1], [2, 2, 3], [1, 1, 3]]