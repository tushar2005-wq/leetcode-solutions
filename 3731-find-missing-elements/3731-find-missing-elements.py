class Solution(object):
    def findMissingElements(self, nums):
        m=min(nums)
        n=max(nums)
        ans=[]
        for i in range(m,n+1):
            if i not in nums:
                ans.append(i)
            else:
                continue
        return ans
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        