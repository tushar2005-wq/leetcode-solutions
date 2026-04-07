class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        combined = nums1 + nums2
        combined.sort()
        n = len(combined)

        if n % 2 == 0:
            mid = n // 2
            median = (combined[mid - 1] + combined[mid]) / 2.0
        else:
            mid = n // 2
            median = combined[mid]

        return median


        