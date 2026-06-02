class Solution(object):
    def minimumTotal(self, triangle):
        ht=len(triangle)
        dp = [[None]*ht for _ in range(ht)]
        def f(i,j):
            if i==(ht-1):
                return triangle[i][j]
            if dp[i][j] is not None:
                return dp[i][j]
            down=triangle[i][j]+ f(i+1,j)
            diag=triangle[i][j] + f(i+1,j+1)
            dp[i][j]=min(down,diag)
            return min(down,diag)
        return f(0,0)
        """
        :type triangle: List[List[int]]
        :rtype: int
        """
        