# https://leetcode.com/problems/find-the-highest-altitude/description/

# Input: gain = [-5,1,5,0,-7]
# Output: 1
# Explanation: The altitudes are [0,-5,-4,1,1,-6]. The highest is 1.

# Input: gain = [-4,-3,-2,-1,4,3,2]
# Output: 0
# Explanation: The altitudes are [0,-4,-7,-9,-10,-6,-3,-1]. The highest is 0.

gain = [-4,-3,-2,-1,4,3,2]

def largestAltitude(gain):
    cur = 0
    cur_max = 0
    for i in gain:
        cur += i
        cur_max = max(cur, cur_max)
    return cur_max



def largestAltitude2(gain):
    cur = 0
    cur_max = 0
    for i in gain:
        cur += i
        cur_max = cur if cur > cur_max else cur_max
    return cur_max