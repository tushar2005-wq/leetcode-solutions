class Solution(object):
    def minPathSum(self, grid):
        n,m=len(grid),len(grid[0])
        dp = [[-1]*m for _ in range(n)]
        def f(i,j):
            if i==0 and j==0:
                return grid[0][0]
            if i<0 or j<0:
                return float('inf')
            if dp[i][j]!=-1:
                return dp[i][j]
            up=grid[i][j]+ f(i-1,j)
            left=grid[i][j] + f(i,j-1)
            dp[i][j]=min(up,left)
            return min(up,left)
        return f(n-1,m-1)
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        