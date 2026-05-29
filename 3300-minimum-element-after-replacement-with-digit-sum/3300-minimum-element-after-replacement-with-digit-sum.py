class Solution(object):
    def minElement(self, nums):
        for i in range(len(nums)):
            sum=0
            for j in str(nums[i]):
                sum+=int(j)
            nums[i]=sum
        return min(nums)
        """
        :type nums: List[int]
        :rtype: int
        """
        