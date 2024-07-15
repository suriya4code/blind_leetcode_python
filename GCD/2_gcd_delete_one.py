A = [7, 21]

def gcd(a, b):
    if b == 0:
        return a
    return gcd(b, a % b)


n = len(A)
if n == 1:
    print(A[0])
if n == 2:
    print(gcd(A[0], A[1]))

prefix = [0] * n
suffix = [0] * n
prefix[0] = A[0]
suffix[-1] = A[-1]

for i in range(1, n):
    prefix[i] = gcd(prefix[i - 1], A[i])
for i in range(n - 2, -1, -1):
    suffix[i] = gcd(suffix[i + 1], A[i])
res = 1
for i in range(1, n-1):
    res = max(res, gcd(prefix[i - 1], suffix[i + 1]))
print(res)
    