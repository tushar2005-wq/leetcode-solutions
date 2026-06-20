class Solution(object):
    def lengthOfLongestSubsequence(self, nums, target):
        dp = [-1] * (target + 1)
        dp[0] = 0

        for num in nums:
            for s in range(target, num - 1, -1):
                if dp[s - num] != -1:
                    dp[s] = max(dp[s], dp[s - num] + 1)

        return dp[target]
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        