class Solution(object):
    def largestAltitude(self, gain):
        altitude=0
        m=0
        for i in gain:
            altitude+=i
            m=max(m,altitude)
        return m
        """
        :type gain: List[int]
        :rtype: int
        """
        