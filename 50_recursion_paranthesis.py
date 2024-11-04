class Solution:
	# @param A : integer
	# @return a list of strings
	def generateParenthesis(self, A):
		self.result = []
		self.printparanthesis(A,0,0,"")
		return self.result

	def printparanthesis(self, n, left, right, s):
		if left == n and right == n:
			self.result.append(s)
			return
		if left < n:
			self.printparanthesis(n, left+1, right, s+'(')
		if right < left:
			self.printparanthesis(n, left, right+1, s+')')

print(Solution().generateParenthesis(3))

