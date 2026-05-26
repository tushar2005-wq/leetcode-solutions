class Solution(object):
    def sumOfUnique(self, nums):
        freq={}
        s=0
        for num in nums:
            if num in freq:
                freq[num]+=1
            else:
                freq[num]=1
        for key,value in freq.items():
            if value<2:
                s+=int(key)
        return s
        """
        :type nums: List[int]
        :rtype: int
        """
        