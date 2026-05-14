class Solution(object):
    def isGood(self, nums):
        nums.sort()

        n = len(nums)

        for i in range(n - 1):
            if nums[i] != i + 1:
                return False

        return nums[-1] == n - 1
        """
        :type nums: List[int]
        :rtype: bool
        """
        