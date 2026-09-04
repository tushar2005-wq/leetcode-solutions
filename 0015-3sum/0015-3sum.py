class Solution(object):
    def threeSum(self, nums):
        nums.sort()
        ans=[]
        for i in range(len(nums)):
            left=i+1
            right=len(nums)-1
            target=-nums[i]
            while(left<right):
                if nums[left]+nums[right]>target:
                    right-=1
                elif nums[left]+nums[right]<target:
                    left+=1
                else:
                    ans.append([nums[i],nums[left],nums[right]])
                    left+=1
                    right-=1
        ans.sort()
        ans = list(set(map(tuple, ans)))
        return ans

                    
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        