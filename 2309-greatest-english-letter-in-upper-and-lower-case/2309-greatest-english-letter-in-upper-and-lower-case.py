class Solution(object):
    def greatestLetter(self, s):
        final=[]
        lower=set()
        upper=set()
        for ch in s:
            if ch.islower():
                lower.add(ch)
            else:
                upper.add(ch)
        for ch in lower:
            if ch.upper() in upper:
                final.append(ch.upper())
        if len(final)==0:
            return ""
        else:
            final=sorted(final)
            return final[-1]

        """
        :type s: str
        :rtype: str
        """
        