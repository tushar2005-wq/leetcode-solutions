class Solution(object):
    def minOperations(self, s):
        ans=''.join(sorted(s))
        if s==ans:
            return 0
        if len(s)==2 and s!=ans:
            return -1
        mn=min(s)
        mx=max(s)
        if s[0]==mn or s[-1]==mx:
            return 1
        if mn in s[1:-1] or mx in s[1:-1]:
            return 2
        return 3
        """
        :type s: str
        :rtype: int
        """
        