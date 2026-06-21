class Solution(object):
    def nextBeautifulNumber(self, n):
        def isbalanced(num):
            freq={}
            for ch in str(num):
                freq[ch]=freq.get(ch,0)+1
            for ch in str(num):
                if freq[ch]!=int(ch):
                    return False
            return True
        curr=n+1
        while True:
            if isbalanced(curr):
                return curr
            curr+=1
        
        """
        :type n: int
        :rtype: int
        """
        