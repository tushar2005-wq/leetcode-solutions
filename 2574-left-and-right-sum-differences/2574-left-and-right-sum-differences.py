class Solution(object):
    def leftRightDifference(self, nums):
        n=len(nums)
        final=[]
        left_sum=0
        right_sum=sum(nums)
        for i in nums:
            right_sum-=i
            final.append(abs(left_sum-right_sum))
            left_sum+=i
        return final
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        