# 1
# 121
# 12321
# 1234321
# 123454321
def solve(n):
    prev = None
    for i in range(1,n+1):
        if prev:
            print(prev + str(i) + prev[::-1])
            prev = prev + str(i)
        else:
            print(str(i))
            prev = str(i)

for i in range(1,int(input())+1):
    #More than 2 lines will result in 0 score. Do not leave a blank line also
    prev = None
    if prev:
        print(prev + str(i) + prev[::-1])
        prev = prev + str(i)
    else:
        print(str(i))
        prev = str(i)
solve(5)
