class Solution():
    def Solve(self, A):
        
        stack = []
        for i in A:
            if stack and stack[-1] == i:
                stack.pop()
            else:
                stack.append(i)
        return ''.join(stack)
        


        

A = "abccbc"        
print(Solution().Solve(A))