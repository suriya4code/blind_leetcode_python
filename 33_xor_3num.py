A = [1, 2, 3, 1, 2, 4]
# A = [2308,1447,1918,1391,2308,216,1391,410,1021,537,1825,1021,1729,669,216,1825,537,1995,805,410,805,602,1918,1447,90,1995,90,1540,1161,1540,2160,1235,1161,602,880,2160,1235,669]
A = [408,478,74,624,74,204,705,624,337,408,478,204]

from functools import reduce
x = reduce(lambda x, y: x ^ y,A)

# find the rightmost set bit
b = 0
while not x & 1<<b:
    b+=1

a = c = 0
for i in A:
    if i & 1<<b:
        a ^= i
    else:
        c ^= i
print(a,c)