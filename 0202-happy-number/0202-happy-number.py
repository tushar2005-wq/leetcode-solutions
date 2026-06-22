class Solution(object):
    def isHappy(self, n):
        seen=set()
        while n!=1 and n not in seen:
            seen.add(n)
            temp=0
            for digit in str(n):
                temp+=int(digit)**2
            n=temp
        return n==1
        """
        :type n: int
        :rtype: bool
        """
        