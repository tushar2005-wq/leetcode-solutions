class Solution(object):
    def uniquePaths(self, m, n):
        dp = [[0]*n for _ in range(m)]

        dp[0][0] = 1   #

        for i in range(m):
            for j in range(n):

                if i == 0 and j == 0:
                    continue

                up = 0
                left = 0

                if i > 0:
                    up = dp[i-1][j]

                if j > 0:
                    left = dp[i][j-1]

                dp[i][j] = up + left

        return dp[m-1][n-1]
        """
        :type m: int
        :type n: int
        :rtype: int
        """
        