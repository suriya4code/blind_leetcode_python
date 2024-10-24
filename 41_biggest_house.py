# luxury house
# code wars site
# https://www.codewars.com/kata/58c8af49fd407dea5f000042/javascript

def solve(h):
    n = len(h)
    mr  = [h[-1]]
    for i in range(n-2,-1,-1):
        mr.insert(0,max(h[i],mr[0]))
    
    res = []
    for j in range(n):
        if h[j] == mr[j]:
            res.append(0)
        else:
            res.append(mr[j]-h[j]+1)
    return res


def solve2(h):
    n = len(h)
    m  = h[-1]
    res = [0]
    for i in range(n-2,-1,-1):
        m = max(m,h[i])
        if h[i] == m:
            res.insert(0,0)
        else:
            res.insert(0,m-h[i]+1)
    return res


h = [3,4,2,5,6,7,1]
print(solve(h))
print(solve2(h))
        
