from functools import cmp_to_key
class Solution(object):
    def largestNumber(self, nums):
        nums=list(map(str,nums)) #because we are sorting for strings
        def compare(a,b):
            if a+b>b+a:
                return -1    #it means 1st will come first
            elif a+b<b+a:
                return 1    #it means 1st will come later
            else:
                return 0
        nums.sort(key=cmp_to_key(compare))
        if nums[0]=="0":  #if largest element is 0 then whole must be 0
            return "0"
        return "".join(nums)
        
        """
        :type nums: List[int]
        :rtype: str
        """
        