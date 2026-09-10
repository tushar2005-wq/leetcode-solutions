class Solution(object):
    def spiralOrder(self, matrix):
        res=[]
        top=0
        bottom=len(matrix)-1
        left=0
        right=len(matrix[0])-1
        while top<=bottom and left<=right:
            for col in range(left,right+1): #left to right
                res.append(matrix[top][col])
            top+=1
            for row in range(top,bottom+1):  #top to bottom
                res.append(matrix[row][right])
            right-=1
            if top<=bottom:
                for col in range(right,left-1,-1): #right to left
                    res.append(matrix[bottom][col])
                bottom-=1
            if left<=right:
                for row in range(bottom,top-1,-1): #bottom to top
                    res.append(matrix[row][left])
                left+=1
        return res                
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        