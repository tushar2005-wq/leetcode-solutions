class Solution(object):
    def maxNumberOfBalloons(self, text):
        main={'b':1,'a':1,'l':2,'o':2,'n':1}
        ans=float('inf')
        sub={}
        for ch in text:
            sub[ch]=sub.get(ch,0)+1
        for ch in main:
            ans=min(ans,sub.get(ch,0) // main[ch])
        return ans
            
        """
        :type text: str
        :rtype: int
        """
        