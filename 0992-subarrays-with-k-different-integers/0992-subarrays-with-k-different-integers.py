class Solution(object):
    def help(self,arr,k):
        l=0
        count=0
        hashmap={}
        for r in range(len(arr)):
            hashmap[arr[r]]=hashmap.get(arr[r],0)+1
            while len(hashmap)>k:
                hashmap[arr[l]]-=1
                if hashmap[arr[l]]==0:
                    del hashmap[arr[l]]
                l+=1
            count+=r-l+1
        return count
            
    def subarraysWithKDistinct(self, nums, k):
        return (self.help(nums,k)-self.help(nums,k-1))
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        