class Solution(object):
     def distinctDifferenceArray(self, nums):
        from collections import Counter

        suffix = Counter(nums)
        prefix = set()
        ans = []

        for x in nums:
            prefix.add(x)

            suffix[x] -= 1
            if suffix[x] == 0:
                del suffix[x]

            ans.append(len(prefix) - len(suffix))

        return ans
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        