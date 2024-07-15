A = [12, 18, 24, 36, 45]

def gcd(a, b):
    if b == 0:
        return a
    return gcd(b, a % b)


result = A[0]
for i in range(1, len(A)):
    result = gcd(result, A[i])
print(result)

