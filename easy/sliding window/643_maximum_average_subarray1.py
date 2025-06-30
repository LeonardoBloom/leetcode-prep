def findMaxAverage(nums, k):
        
        # nums = [] with n elements
        # int k
        # find [x, y, z] with len = k with max ave (x + y + z) / k
        # return ave

        currSum = sum(nums[:k])
        maxSum = currSum

        for i in range(k, len(nums)):
            currSum += nums[i] - nums[i-k]

            maxSum = (max(maxSum, currSum))

        return maxSum / k
            

nums = [1,12,-5,-6,50,3]

print(findMaxAverage(nums, 4))