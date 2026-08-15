class Solution(object):
    def reverseVowels(self, s):
        l=0
        r=len(s)-1
        s=list(s)
        while l<=r:
            if s[l].lower() in 'aeiou' and s[r].lower() in 'aeiou':
                s[l],s[r]=s[r],s[l]
                l+=1
                r-=1
            elif s[l].lower() in 'aeiou' and s[r].lower() not in 'aeiou' :
                r-=1
            else:
                l+=1
        return "".join(s)
        """
        :type s: str
        :rtype: str
        """
        