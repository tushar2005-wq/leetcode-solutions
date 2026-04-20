class Solution(object):
    def maximumDifference(self, nums):
        ans=-1
        for i in range(len(nums)):
            for j in range(i+1,len(nums)):
                if nums[i]<nums[j]:
                    dist=nums[j]-nums[i]
                    ans=max(ans,dist)
        return ans
        """
        :type nums: List[int]
        :rtype: int
        """
        