'''
Input: nums = [2, 7, 11, 15], target = 9    Output: [0, 1]
Input: nums = [3, 2, 4], target = 6         Output: [1, 2]
Input: nums = [3, 3], target = 6            Output: [0, 1]

'''


def two_sum(nums: list, target:int):
    seen = {}
    n = len(nums)
    for i in range(n):
        if nums[i] in seen:
            return [seen[nums[i]],i]
        else:
            seen[target - nums[i]] = i
    return []

nums = [3, 2, 4]
target = 6
print(two_sum(nums, target))


def two_sum_eff(nums:list, target:int):
    needed = {}
    for i, num in enumerate(nums):
        if num in needed:
            return [needed(num), i]
        needed[target - num] = i
        return []