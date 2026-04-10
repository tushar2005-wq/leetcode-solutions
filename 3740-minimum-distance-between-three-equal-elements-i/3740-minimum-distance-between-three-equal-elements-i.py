class Solution(object):
    def minimumDistance(self, nums):
        ans=float('inf')
        dist=0
        n=len(nums)
        for i in range(n):
            for j in range(i+1,n):
                for k in range(j+1,n):
                    if nums[i]==nums[j]==nums[k]:
                        dist=2*(k-i)
                        ans=min(dist,ans)
        return ans if ans!=float('inf') else -1
        """
        :type nums: List[int]
        :rtype: int
        """
        