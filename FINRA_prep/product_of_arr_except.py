'''
Input: nums = [1, 2, 3, 4]          Output: [24, 12, 8, 6]
Input: nums = [-1, 1, 0, -3, 3]     Output: [0, 0, 9, 0, 0]
'''

def product_except_self(nums: list[int]) -> list[int]:
    n = len(nums)
    ps = [1] * n
    last = 1

    for i in range(n):
        ps[i] = last
        last *= nums[i]

    ss = [1] * n
    prev = 1

    for j in range(n-1,-1,-1):
        ss[j] *= prev
        prev *= nums[j]

    return ps, ss



nums = [1, 2, 3, 4] 

print(product_except_self(nums))