class Solution(object):
    def runningSum(self, nums):
        final=[]
        s=0
        for i in range(len(nums)):
            s+=nums[i]
            final.append(s)
        return final
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        