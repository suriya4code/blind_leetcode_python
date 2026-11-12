def twoNumberSum(array, targetSum):
    # Write your code here.
    h = {}
    for i in array:
        if h.get(targetSum-i,None) != None:
            return [i, targetSum-i]
            
        else:
            h[i] = targetSum-i
    return []


print(twoNumberSum([3, 5, -4, 8, 11, 1, -1, 6], 10))
# Output: [-1, 11]

for i in range(10):
    pass
print(i)