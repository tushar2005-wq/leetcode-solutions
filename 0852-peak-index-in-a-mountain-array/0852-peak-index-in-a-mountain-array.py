class Solution(object):
    def peakIndexInMountainArray(self, arr):
        l,h=0,len(arr)-1
        while l<h:
            mid=(l+h)//2
            if arr[mid]>arr[mid+1]:
                h=mid
            else:
                l=mid+1
        return l
        """
        :type arr: List[int]
        :rtype: int
        """
        