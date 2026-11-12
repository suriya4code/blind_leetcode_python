# Input: s = "abcabcbb"
# Output: 3

def solve(s):
    n = len(s)
    h = {}
    start = 0
    res = 0

    for i,c in enumerate(s):
        if c in h and h[c] >= start:
            start = h[c] + 1
        else:
            res = max(i-start+1, res)
        h[c] = i
    
    return res
            
s = "au"
# s = "abcabcbb"
# s = "dvdf"
s = "tmmzuxt"
print(solve(s))
