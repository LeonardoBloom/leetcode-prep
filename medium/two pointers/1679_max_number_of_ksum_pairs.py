def maxOperations(nums, k):

    l = 0
    r = len(nums) - 1
    ops = 0
    nums.sort()

    while l < r:
        sums = nums[l] + nums[r]

        if sums < k:
            l += 1
        elif sums > k:
            r -= 1
        elif sums == k:
            ops += 1
            l += 1
            r -= 1
    
    return ops


nums = [3, 1, 3, 4, 3]
nums = [1,2,3,4]
nums = [4,4,1,3,1,3,2,2,5,5,1,5,2,1,2,3,5,4]
k = 2


print(nums)
print(maxOperations(nums, k))