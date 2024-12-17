class Solution:
    # @param A : string
    # @return an integer
    def solve(self, A):
            h = {'{' : 1, '}' : -1, '(':1, ')':-1, '[':1,']':-1}
            ans = 0
            for i in A:
                  if ans < 0:
                        return 0
                  ans += h[i]
            return 1 if ans == 0 else 0
    
    def solve2(self, A):
        stack = []
        brackets = {
            ')': '(',
            '}': '{',
            ']': '['
        }
        for char in A:
            if char in brackets.values():
                stack.append(char)
            elif char in brackets.keys():
                if not stack or brackets[char] != stack.pop():
                    return 0

        return 1 if stack == [] else 0

    def solve3(self, A):
         stack = []
         closing_opening = {
            ')': '(',
            '}': '{',
            ']': '['
            }
         for i in A:
             if i in closing_opening.values():
                   stack.append(i)
             else:
                  if not stack or closing_opening[i] != stack.pop():
                       return 0
         return 1 if stack == [] else 0

        

        
          


A = '{([])}'
# A = '({)}'
print(Solution().solve(A))
print(Solution().solve2(A))