def pow(A, B, C):
    if A == 0:
        return 0
    if B == 0:
        return 1
    elif B % 2 == 0:
        temp = pow(A, B // 2, C)
        return (temp * temp) % C
    else:
        temp = pow(A, B - 1, C)
        return (A * temp) % C

def powmod(A, B, C):
    if B == 0:
        return 1
    p = powmod(A, B // 2, C) % C
    p = (p * p) % C
    return p if B % 2 == 0 else (A * p) % C


print(powmod(21, 35, 3))

A = 3
B = 5

# A^B % C = (A % C)^B % C

#A-1 mod B

