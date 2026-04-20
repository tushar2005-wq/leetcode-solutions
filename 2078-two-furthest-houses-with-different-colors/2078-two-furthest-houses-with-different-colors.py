class Solution(object):
    def maxDistance(self, colors):
        n=len(colors)
        ans=float('-inf')
        for i in range(n):
            for j in range(i+1,n):
                if colors[i]!=colors[j]:
                    dist=abs(i-j)
                    ans=max(ans,dist)
        return ans
        """
        :type colors: List[int]
        :rtype: int
        """
        