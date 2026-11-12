class Solution:
    # @param N : list of integers
    # @return a list of integers
    def solve(self, N):
        # spf array
        spf = [ i for i in range(N+1)]

        for i in range(2,N+1):
            if spf[i] == i:
                for j in range(i,N+1,i):
                    spf[j] = i
        ans = 1
        while N>1:
            cnt = 0
            x = spf[N]
            while N%x == 0:
                N = N//x
                cnt +=1
            ans = ans * (cnt + 1)
        return ans
    
print(Solution().solve(9)) # 9


def solve(A):
    res = []
    for N in A:
        divisors = [2] * (N+1)
        divisors[1] = 1
        for i in range(2, N+1):
            for j in range(2*i, N+1, i):
                divisors[j] += 1
        res.append(sum(divisors))
    return res

print(solve([9,4])) # 9

