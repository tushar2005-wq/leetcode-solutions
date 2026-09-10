class Solution(object):
    def findPeakElement(self, nums):
        m=max(nums)
        for i,val in enumerate(nums):
            if val==m:
                return i
        
        

        """
        :type nums: List[int]
        :rtype: int
        """
        