def productExceptSelf(nums):
        
        result = [1] * len(nums)
        prod = 1

        for x in range(len(result)):
            result[x] = result[x] * prod
            prod = prod * nums[x]

        prod = 1
        for x in range(len(result) -1 , -1, -1):
            result[x] = result[x] * prod
            prod = prod * nums[x]

        return result