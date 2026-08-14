class Solution(object):
    def longestOnes(self, nums, k):
        l=0
        zeros=0
        ans=0
        for r in range(len(nums)):
            if nums[r]==0:
                zeros+=1
            while zeros>k:
                if nums[l]==1:
                    l+=1
                else:
                    zeros-=1
                    l+=1
            ans=max(ans,r-l+1)
        return ans

        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        