class Solution(object):
    def maxSubsequence(self, nums, k):
        res=[]
        num_with_index=[(num,i) for i,num in enumerate(nums)]
        num_with_index.sort(key=lambda x:-x[0])
        top_k_elements=sorted(num_with_index[:k],key=lambda x:x[1])
        for i in top_k_elements:
            res.append(i[0])
        return res
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        