A = 36

count = 2
for i in range(2,int(A**0.5 + 1)):
    if A % i == 0:
        count += 2
    if i * i == A:
        count -= 1

print(count)