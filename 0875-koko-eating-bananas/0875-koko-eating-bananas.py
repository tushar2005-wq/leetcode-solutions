import math

class Solution(object):
    def minEatingSpeed(self, piles, h):
        low = 1
        high = max(piles)
        ans = high

        while low <= high:
            mid = (low + high) // 2
            hours = 0

            for p in piles:
                hours += (p + mid - 1) // mid   # ceil(p/mid)

            if hours <= h:
                ans = mid
                high = mid - 1
            else:
                low = mid + 1

        return ans
        
        """
        :type piles: List[int]
        :type h: int
        :rtype: int
        """
        