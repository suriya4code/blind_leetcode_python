# https://leetcode.com/problems/find-the-highest-altitude/description/

# Input: gain = [-5,1,5,0,-7]
# Output: 1
# Explanation: The altitudes are [0,-5,-4,1,1,-6]. The highest is 1.

# Input: gain = [-4,-3,-2,-1,4,3,2]
# Output: 0
# Explanation: The altitudes are [0,-4,-7,-9,-10,-6,-3,-1]. The highest is 0.

gain = [-4,-3,-2,-1,4,3,2]

def largestAltitude(gain):
    current_altitude = 0
    max_altitude = 0
    for altitude_gain in gain:
        current_altitude += altitude_gain
        max_altitude = max(current_altitude, max_altitude)
    return max_altitude
