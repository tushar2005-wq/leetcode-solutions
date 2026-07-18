class Solution(object):
    def setZeroes(self, matrix):
        rows = set()
        cols = set()
        
        n = len(matrix)   #number of rows 
        m = len(matrix[0])  #number of cols
        
        # First pass
        for i in range(n):
            for j in range(m):
                if matrix[i][j] == 0:
                    rows.add(i)
                    cols.add(j)
        
        # Zero rows
        for r in rows:
            for j in range(m):
                matrix[r][j] = 0
        
        # Zero columns
        for c in cols:
            for i in range(n):
                matrix[i][c] = 0

        """
        :type matrix: List[List[int]]
        :rtype: None Do not return anything, modify matrix in-place instead.
        """
        