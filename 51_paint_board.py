class Solution:
    # @param A : integer
    # @param B : integer
    # @param C : list of integers
    # @return an integer
    def paint(self, A, B, C):
        mod = 10000003
        ans = 0
        def check(N,A,C,M):
            c = 0
            s =0
            for i in range(N):
                s+=C[i]
                if s>M:
                    c+=1
                    s=C[i]
                    if c == A:
                        return False

            return True            

        l = 1
        h = 0
        for i in range(len(C)):
            C[i] = B*C[i]
            l = max(C[i],l)
            h+=C[i]

        #let us apply the mighty binary search:
        while(l<=h):
            m = (l+h)//2
            if check(len(C),A,C,m) == True:
                ans = m
                h = m-1
            else:
                l = m+1

        return ans%mod            

print(Solution().paint(3,10,[640,435,647,352,8,90,960,329,859])) # 1720
