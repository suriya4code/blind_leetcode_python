class Solution:
	# @param A : tuple of integers
	# @return an integer
	def longestConsecutive(self, A):
		n = len(A)
		cnt = 0
		m = 0
		for i in range(1,n):
			if (A[i] == A[i-1]+1):
				cnt+=1
			else:
				cnt = 0
			m = max(m,cnt)
		return m+1
            
            
            


print(Solution().longestConsecutive([100, 4, 200, 1, 3, 2])) # 4