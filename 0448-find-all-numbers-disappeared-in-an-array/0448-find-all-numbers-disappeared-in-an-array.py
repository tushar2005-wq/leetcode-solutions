class Solution(object):
    def findDisappearedNumbers(self, nums):
        s=set(nums)
        n=len(nums)
        ans=[]
        for i in range(1,n+1):
            if i not in s:
                ans.append(i)
        return ans
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        