from collections import defaultdict
import bisect
class Solution(object):
    def solveQueries(self, nums, queries):
        n = len(nums)
        
        # Step 1: map value -> indices
        pos = defaultdict(list)
        for i, num in enumerate(nums):
            pos[num].append(i)
        
        res = []
        
        for q in queries:
            arr = pos[nums[q]]
            
            # If only one occurrence
            if len(arr) == 1:
                res.append(-1)
                continue
            
            # Step 2: binary search
            idx = bisect.bisect_left(arr, q)
            
            # neighbors (circular)
            left = arr[idx - 1] if idx > 0 else arr[-1]
            right = arr[idx + 1] if idx < len(arr) - 1 else arr[0]
            
            # Step 3: compute distances
            d1 = abs(q - left)
            d2 = abs(q - right)
            
            d1 = min(d1, n - d1)
            d2 = min(d2, n - d2)
            
            res.append(min(d1, d2))
        
        return res
        """
        :type nums: List[int]
        :type queries: List[int]
        :rtype: List[int]
        """
        