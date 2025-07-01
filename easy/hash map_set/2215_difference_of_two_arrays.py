def findDifference(nums1, nums2):
        """
        answer = [ [num1NOT2] , [num2NOT1] ]

        """

        # make each array present only unique values
        ans1 = set(nums1)
        ans2 = set(nums2)

        # add to ans1 and ans2 values not present in each other from num1 and nums2 respectively
        for x in nums2:
            if x in ans1:
                ans1.remove(x)
                ans2.discard(x) # avoid loop exceptions

        return [list(ans1), list(ans2)]
