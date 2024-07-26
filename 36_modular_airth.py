# very large sum



def power(x, y, p) : 
    res = 1     # Initialize result 
  
    # Update x if it is more 
    # than or equal to p 
    x = x % p  
      
    if (x == 0) : 
        return 0
  
    while (y > 0) : 
          
        # If y is odd, multiply 
        # x with result 
        if ((y & 1) == 1) : 
            res = (res * x) % p 
  
        # y must be even now 
        y = y >> 1      # y = y/2 
        x = (x * x) % p 
          
    return res

class Solution2:
    # @param A : integer
    # @param B : integer
    # @return an integer
    
    def solve(self, A, B):
        fact = 1
        mod = 1000000007
        # calculating factorial of B
        for i in range(2, B + 1):
            fact = (fact * i) % (mod - 1)   # (mod-1) is used accoring to Fermat Little theorem.
        return power(A, fact, mod)  # calculating power by divide and conquer





class Solution:
    # @param A : integer
    # @param B : integer
    # @return an integer
    def pow(self, A, B, C):
        ans = 1
        A = A % C
        if A == 0:
            return 0
        if B == 0:
            return 1
        while B > 0:
            if (B & 1) == 1:
                ans = (ans * A) %C
            B = B >> 1
            A = (A * A) % C
        return ans

    def solve(self, A, B):
        mod = 1000000007
        fact = 1
        for i in range(2,B+1):
            fact = (fact * i) % (mod-1)

        # power
        return self.pow(A,fact,mod)
    
print(Solution().solve(2, 27)) # 8
print(Solution2().solve(2, 27)) # 8
