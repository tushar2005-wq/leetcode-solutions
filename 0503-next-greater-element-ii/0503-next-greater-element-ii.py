class Solution(object):
    def nextGreaterElements(self, nums):
        n=len(nums)
        stack=[]
        final_ans=[]
        c_nums=nums+nums
        ans=[-1]*len(c_nums)
        for i in range(len(c_nums)-1,-1,-1):
            while stack and stack[-1]<=c_nums[i]:
                stack.pop()
            ans[i]=-1 if not stack else stack[-1]
            stack.append(c_nums[i])
        for j in range(n):
            final_ans.append(ans[j])
        return final_ans
            
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        