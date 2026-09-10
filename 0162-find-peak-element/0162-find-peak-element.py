class Solution(object):
    def findPeakElement(self, nums):
        l,h=0,len(nums)-1
        while l<h:
            mid=(l+h)//2
            if nums[mid]>nums[mid+1]:
                h=mid
            else:
                l=mid+1
        return l
        
        

        """
        :type nums: List[int]
        :rtype: int
        """
        