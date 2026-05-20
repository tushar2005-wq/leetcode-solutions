class Solution(object):
    def findThePrefixCommonArray(self, A, B):
        n=len(A)
        ans=[]
        freq=[0]*(n+1)
        c=0
        for i in range(n):
            freq[A[i]]+=1
            if freq[A[i]]==2:
                c+=1
            freq[B[i]]+=1
            if freq[B[i]]==2:
                c+=1
            ans.append(c)
        return ans
        """
        :type A: List[int]
        :type B: List[int]
        :rtype: List[int]
        """
        