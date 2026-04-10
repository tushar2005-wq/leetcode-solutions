from collections import defaultdict
class Solution(object):
    def minimumDistance(self, nums):
        pos=defaultdict(list)
        for i,num in enumerate(nums):
            pos[num].append(i)
        ans=float('inf')
        for index in pos.values():
            if len(index)>=3:
                for i in range(len(index)-2):
                    dist=2*(index[i+2]-index[i])
                    ans=min(ans,dist)
        return ans if ans!=float('inf') else -1
        """
        :type nums: List[int]
        :rtype: int
        """
        