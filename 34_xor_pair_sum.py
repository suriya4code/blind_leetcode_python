A = [1, 2, 3]
A = [3, 4, 2]
#sum of xor of all pairs

ans = 0
for i in range(32):
    count = 0
    for j in A:
        if j & 1<<i:
            count += 1
    ans = ans+ (count * (len(A) - count) * 2**i)
print(ans)