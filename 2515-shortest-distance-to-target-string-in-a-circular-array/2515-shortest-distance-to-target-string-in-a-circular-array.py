class Solution(object):
    def closestTarget(self, words, target, startIndex):
        n=len(words)
        if target not in words:
            return -1
        ans=float('inf')
        for i in range(n):
            if words[i]==target:
                dist=min(abs(i-startIndex),n-abs(i-startIndex))   #concept of circular distance
                ans=min(ans,dist)
        return ans
        """
        :type words: List[str]
        :type target: str
        :type startIndex: int
        :rtype: int
        """
        