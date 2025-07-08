def maxArea(height):
        """
        :type height: List[int]
        :rtype: int
        """
        l = 0
        r = len(height) - 1
        maxArea = 0

        while l < r:
            area = min(height[l], height[r]) * (r-l)
            maxVol = max(maxVol, area)

            if height[l] <= height[r]:
                l += 1
            elif height[r] <= height[l]:
                r -= 1
                
        return maxVol