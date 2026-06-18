class Solution(object):
    def findTargetSumWays(self, nums, target):
        n=len(nums)
        dp={}
        def solve(i,target):
            if i < 0:
                return 1 if target == 0 else 0
            if(i,target) in dp:
                return dp[(i,target)]
            minus=solve(i-1,target-nums[i])
            plus=solve(i-1,target+nums[i])
            dp[(i,target)]=minus + plus
            return dp[(i,target)]
        return solve(n-1,target)
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        