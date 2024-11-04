# You are given three positive integers, A, B, and C.

# Any positive integer is magical if divisible by either B or C.
class Solution:
    # @param A : integer
    # @param B : integer
    # @param C : integer
    # @return an integer
    def solve(self, A, B, C):
        mod = (10**9)+7
        gcd = self.gcd(B,C)
        lcm = (B*C)//gcd

        l = 1
        h = min(B,C)*A
        floor = 0
        while l <= h:
            m = l + ((h-l)//2)
            magic = self.magic_count(m,B,C,lcm)

            if magic >= A:
                floor = m
                h = m-1
            else:
                l = m+1

        return floor%mod
    
    def gcd(self,b,c):
        if c == 0:
            return b

        return self.gcd(c,b%c)

    def magic_count(self,a,b,c,lcm):
        return ((a//b) + (a//c) - (a//lcm))


A= 807414236
B= 3788
C= 38141
A= 10
B= 2
C= 3
print(Solution().solve(A,B,C)) # 15