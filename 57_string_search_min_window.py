class Solution():
    def Solve(self, A, B):
        hm={}
        n=len(A)
        m=len(B)
        min_len=10**9
       
# freq map for B
        for i in range(m):
            if B[i] in hm:
                hm[B[i]]+=1
            else:
                hm[B[i]]=1
       
        l=0
        r=0
        start_index=-1
        cnt=0
        while r<n:
            if A[r] in hm:
                if hm[A[r]] > 0:
                    cnt+=1
                hm[A[r]]-=1

            while cnt==m: # if found will loop the till more less char string didn't found
                if (r-l+1)<min_len:
                    min_len=r-l+1
                    start_index=l

                if A[l] in hm:
                    hm[A[l]]+=1
                    if (hm[A[l]])>0:
                        cnt-=1
                l+=1
            r+=1
        if start_index==-1:
            return ""
        else:
            return A[start_index:start_index+min_len]


A = "ADOBECODEBANC"
B = "ABC"
print(Solution().Solve(A, B))