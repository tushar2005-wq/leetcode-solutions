class Solution(object):
    def minSubArrayLen(self, target, nums):
        left = 0
        sum = 0
        ans = float('inf')

        for right in range(len(nums)):
            sum += nums[right]

            while sum >= target:
                ans = min(ans, right - left + 1)
                sum -= nums[left]
                left += 1

        return 0 if ans == float('inf') else ans


        """
        :type target: int
        :type nums: List[int]
        :rtype: int
        """
        