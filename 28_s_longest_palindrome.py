
class Solution:
	# @param A : string
	# @return a strings
	def longestPalindrome(self, A):
		n = len(A)
		res = ""
		for i in range(n):
            # odd
			tmp = self.check_pal(A, i, i)
			if len(tmp)>len(res):
				res = tmp
			# even
			tmp = self.check_pal(A,i,i+1)
			if len(tmp)>len(res):
				res = tmp
		return res
	
	def check_pal(self, A, l, r):
		while l>=0 and r<len(A) and A[l] == A[r]:
			l -= 1
			r += 1
		return A[l+1:r]
		
		
	
A = "abcbedrardea"
print(Solution().longestPalindrome(A))