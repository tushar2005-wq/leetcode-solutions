class Solution(object):
    def minimumTotal(self, triangle):
        ht=len(triangle)
        dp=triangle[-1]
        for i in range(ht-2,-1,-1):
            for j in range(len(triangle[i])):
                dp[j]=triangle[i][j] + min(dp[j],dp[j+1])
        return dp[0]
        """
        :type triangle: List[List[int]]
        :rtype: int
        """
        