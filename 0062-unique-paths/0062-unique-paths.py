class Solution(object):
    def uniquePaths(self, m, n):
        dp = [[-1]*n for _ in range(m)]
        def f(i,j):
            if i==0 and j==0:
                return 1
            if i<0 or j<0:
                return 0
            if dp[i][j]!=-1:
                return dp[i][j]
            up=f(i-1,j)
            left=f(i,j-1)
            dp[i][j]=up+left
            return left+up
        return f(m-1,n-1)
        """
        :type m: int
        :type n: int
        :rtype: int
        """
        