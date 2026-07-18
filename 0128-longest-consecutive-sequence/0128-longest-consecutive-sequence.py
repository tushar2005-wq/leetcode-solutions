class Solution(object):
    def longestConsecutive(self, nums):
        s = set(nums)
        ans = 0

        for num in s:
            if num - 1 not in s:
                curr = num
                length = 1

                while curr + 1 in s:
                    curr += 1
                    length += 1

                ans = max(ans, length)

        return ans
        """
        :type nums: List[int]
        :rtype: int
        """
        