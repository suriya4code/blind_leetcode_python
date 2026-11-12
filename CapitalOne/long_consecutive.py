nums = [0,0]


def Solve(nums: list):
    if len(nums) in (0,1):
        return len(nums)
    arr = nums
    arr.sort()
    curr_max = 1
    prev = arr[0]
    curr = 1
    for i in arr[1:]:
        if i == prev:
            continue
        if prev +1 == i:
            curr += 1
            if curr > curr_max:
                curr_max = curr
        else:
            curr = 1
        prev = i
    return curr_max

print(Solve(nums))