class Solution(object):
    def rotate(self, nums, k):
        l=len(nums)
        k=k%l
        def reverse(left,right):
            while left<right:
                nums[left],nums[right]=nums[right],nums[left]
                left+=1
                right-=1
        reverse(0,l-1)
        reverse(0,k-1)
        reverse(k,l-1)
        """
        :type nums: List[int]
        :type k: int
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        