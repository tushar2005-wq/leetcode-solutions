class Solution(object):
    def findColumnWidth(self, grid):
        row=len(grid)
        cols=len(grid[0])
        final=[]
        for j in range(cols):
            width=0
            for i in range(row):
                width=max(width,len(str(grid[i][j])))
            final.append(width)
        return final
        """
        :type grid: List[List[int]]
        :rtype: List[int]
        """
        