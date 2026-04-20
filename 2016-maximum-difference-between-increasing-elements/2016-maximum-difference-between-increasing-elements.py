class Solution(object):
    def maximumDifference(self, nums):
        min_val=nums[0]
        diff=-1
        for i in range(1,len(nums)):
            if nums[i]>min_val:
                diff=max(diff,nums[i]-min_val)
            else:
                min_val=nums[i]
        return diff

        """
        :type nums: List[int]
        :rtype: int
        """
        