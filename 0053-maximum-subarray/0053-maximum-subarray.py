class Solution(object):
    def maxSubArray(self, nums):
        current_sum=max_sum=nums[0]
        for num in nums[1:]:
            current_sum=max(num,current_sum+num)
            max_sum=max(current_sum,max_sum)
        return max_sum
        """
        :type nums: List[int]
        :rtype: int
        """
        