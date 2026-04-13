class Solution(object):
    def getMinDistance(self, nums, target, start):
        res=[]
        ans=float('inf')
        for i in range(len(nums)):
            if nums[i]==target:
                res.append(i)
        for j in res:
            val=abs(j-start)
            ans=min(ans,val)
        return ans
        """
        :type nums: List[int]
        :type target: int
        :type start: int
        :rtype: int
        """
        