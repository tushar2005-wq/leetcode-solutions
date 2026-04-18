class Solution(object):
    def mirrorDistance(self, n):
        s=str(n)
        rev_s=s[::-1]
        return abs(n-int(rev_s))
        """
        :type n: int
        :rtype: int
        """
        