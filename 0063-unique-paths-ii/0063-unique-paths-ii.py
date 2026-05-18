class Solution(object):
    def uniquePathsWithObstacles(self, obstacleGrid):
        m,n=len(obstacleGrid),len(obstacleGrid[0])
        dp = [[-1]*n for _ in range(m)]
        def f(i,j):
            if i<0 or j<0 or obstacleGrid[i][j]==1:
                return 0
            if i==0 and j==0:
                return 1
            if dp[i][j]!=-1:
                return dp[i][j]
            left=f(i-1,j)
            up=f(i,j-1)
            dp[i][j]=left+up
            return up+left
        return f(m-1,n-1)
        """
        :type obstacleGrid: List[List[int]]
        :rtype: int
        """
        