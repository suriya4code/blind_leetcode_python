"""
Example 1:

Input: nums = [1,2,3,4]
Output: [24,12,8,6]
Example 2:

Input: nums = [-1,1,0,-3,3]
Output: [0,0,9,0,0]
"""

from time import time
from typing import List


class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        left = [nums[0]]
        for i in range(1,n):
            left.append(nums[i]*left[i-1])
        right = [nums[-1]]
        for j in range(n-2,-1,-1):
            right.insert(0,(nums[j]*right[0]))
        res = [right[1]]
        for k in range(1,n-1):
            res.append(left[k-1]*right[k+1])
        res.append(left[-1])
        return res

def calc_time(func):
     def inner(*args, **kwargs):
          start = time()
          func(*args, **kwargs)
          end = time()
          print(f"Completed in {str((end-start)*1000)} s time")
     return inner

@calc_time
def solution2(nums):
        n = len(nums)
        prefix_product = 1
        postfix_product = 1
        result = [0]*n
        for i in range(n):
            result[i] = prefix_product
            prefix_product *= nums[i]
        for i in range(n-1,-1,-1):
            result[i] *= postfix_product
            postfix_product *= nums[i]
        return result

nums = [-1,1,0,-3,3]
print(Solution().productExceptSelf(nums))
print(solution2(nums))