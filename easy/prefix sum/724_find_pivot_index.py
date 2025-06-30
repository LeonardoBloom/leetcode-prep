
def pivotIndex(nums):
    """
    <--- Lsum [index] Rsum ->
    Lsum = Rsum 

    """
    lsum = 0
    currSum = sum(nums)

    for i in range(len(nums)):
        rsum = currSum - lsum - nums[i]
    

        if lsum == rsum:
            return i
        
        lsum += nums[i]

    return -1