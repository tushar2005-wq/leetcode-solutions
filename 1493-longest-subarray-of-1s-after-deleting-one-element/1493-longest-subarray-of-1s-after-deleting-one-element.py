class Solution(object):
    def longestSubarray(self, nums):
        l=0
        ans=0
        d=0
        for r in range(len(nums)):
            if nums[r]==0:
                d+=1
            while d>1:
                if nums[l]==0:
                    d-=1
                l+=1
            ans=max(ans,r-l)
        return ans
        """
        :type nums: List[int]
        :rtype: int
        """
        