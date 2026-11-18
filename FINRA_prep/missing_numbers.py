'''
Input: nums = [3, 0, 1]                      Output: 2
Input: nums = [0, 1]                         Output: 2
Input: nums = [9, 6, 4, 2, 3, 5, 7, 0, 1]    Output: 8
'''

def missing_number(ip:list):
    n = len(ip)
    ip.sort()
    comp = [i for i in range(n) ]
    for i in range(n):
        if comp[i] != ip[i]:
            return i
    return -1

def missing_numbers_quick(ip:list):
    n = len(ip)
    return (n * (n+1) // 2 ) - sum(ip)


nums = [9, 6, 4, 2, 3, 5, 7, 0, 1]  
print(missing_number(nums))
print(missing_numbers_quick(nums))