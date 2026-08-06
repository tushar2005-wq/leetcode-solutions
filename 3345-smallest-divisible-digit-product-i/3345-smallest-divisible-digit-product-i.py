class Solution(object):
    def smallestNumber(self, n, t):
        for i in range(n,101):
            product=1
            for j in str(i):
                product*=int(j)
            if product%t==0:
                return i
    
        """
        :type n: int
        :type t: int
        :rtype: int
        """
        