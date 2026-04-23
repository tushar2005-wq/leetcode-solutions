from collections import defaultdict

class Solution(object):
    def distance(self, nums):
        mp = defaultdict(list)
        for i, num in enumerate(nums):
            mp[num].append(i)
        res = [0] * len(nums)
        for indices in mp.values():
            n = len(indices)
            prefix = [0] * (n + 1)
            for i in range(n):
                prefix[i+1] = prefix[i] + indices[i]
            for i in range(n):
                idx = indices[i]
                # left side
                left = idx * i - prefix[i]
                # right side
                right = (prefix[n] - prefix[i+1]) - idx * (n - i - 1)
                res[idx] = left + right
        return res
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        