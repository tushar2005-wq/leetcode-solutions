class Solution(object):
    def reverseWords(self, s):
        rev_str=s.split()
        rev_str.reverse()
        final=" ".join(rev_str)
        return final
        """
        :type s: str
        :rtype: str
        """
        