class Solution:
    def maxArea(self, height):
        l,r=0,len(height)-1
        max_area=0
        while l<r:
            w=r-l
            h=min(height[l],height[r])
            max_area=max(max_area,h*w)
            if height[l]<height[r]:
                l+=1
            else:
                r-=1
        return max_area
        """
        :type height: List[int]
        :rtype: int
        """
        