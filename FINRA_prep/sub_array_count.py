'''
P9. Subarray sum equals K
Medium
Count the contiguous, non-empty subarrays of nums whose sum equals k. Numbers can be negative.
Signature: subarray_sum(nums: list[int], k: int) -> int
Input: nums = [1, 1, 1], k = 2      Output: 2
Input: nums = [1, 2, 3], k = 3      Output: 2      ([1, 2] and [3])
Input: nums = [1, -1, 0], k = 0     Output: 3      ([1, -1], [1, -1, 0] and [0])

'''

from collections import Counter

def subarray_sum(nums: list[int], k: int) -> int:
    count = running = 0
    seen = Counter({0: 1})  # prefix sum -> times seen
    for x in nums:
        running += x
        count += seen[running - k]
        seen[running] += 1
    return count

# Tests: ([1, 1, 1], 2) -> 2, ([1, 2, 3], 3) -> 2, ([1, -1, 0], 0) -> 3
        



nums = [1, 2, 3]
k = 3 
print(subarray_sum(nums,k))