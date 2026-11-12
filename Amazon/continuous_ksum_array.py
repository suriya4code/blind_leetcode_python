
# Given an array of integers and an integer k, you need to find the total number of continuous subarrays whose sum equals to k.


def subarraySum(arr, k):
    temp_sum = 0
    for i in arr:
        temp_sum += i
        if temp_sum == k:
            count += 1
        if temp_sum > k:
            temp_sum - i
        



arr = [10, 2, -2, -20, 10]
k = -10

# Output: 3