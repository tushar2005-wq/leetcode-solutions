class Solution(object):
    def restoreString(self, s, indices):
        final=[""]*len(indices)
        n=len(indices)
        for i in range(n):
            final[indices[i]]=s[i]
        return "".join(final)
        """
        :type s: str
        :type indices: List[int]
        :rtype: str
        """
        