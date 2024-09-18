





def fibonocci(n):
    if n == 0:
        return 0
    if n == 1:
        return 1
    return fibonocci(n-1) + fibonocci(n-2)
def solve (A):
    # sum of fibonocci
    return fibonocci(A-1) + fibonocci(A-2)
print(solve(9)) # 2