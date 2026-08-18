class Solution(object):
    def largestInteger(self, nums, k):
        hashmap={}
        for i in range(len(nums)-k+1):
            subarr=nums[i:i+k]
            for x in set(subarr):
                hashmap[x]=hashmap.get(x,0)+1
        ans=-1
        for x in hashmap:
            if hashmap[x]==1:
                ans=max(ans,x)
        return ans
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        