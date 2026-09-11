class Solution(object):
    def longestPalindrome(self, s): #expand from the centre
        n=len(s)
        max_ans=""
        for i in range(n): # case for the odd length
            low=i
            high=i
            while low>=0 and high<n and s[low]==s[high]:
                if high-low+1>len(max_ans):
                    max_ans=s[low:high+1]
                low-=1
                high+=1
            low=i
            high=i+1
            while low>=0 and high<n and s[low]==s[high]: #case for the even length
                if high-low+1>len(max_ans):
                    max_ans=s[low:high+1]
                low-=1
                high+=1
        return max_ans
        """
        :type s: str
        :rtype: str
        """
        
        