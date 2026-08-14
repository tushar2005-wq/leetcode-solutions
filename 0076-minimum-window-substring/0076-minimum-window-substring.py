from collections import defaultdict
class Solution(object):
    def check(self,map_s,map_t):
        count=0
        for x in map_t:
            if map_s[x]>=map_t[x]:
                count+=1
        return count==len(map_t)
    def minWindow(self, s, t):
        ret=""
        map_t=defaultdict(int)
        for i in t:
            map_t[i]=map_t.get(i,0)+1
        map_s=defaultdict(int)
        l=0
        ans=float('inf')
        for r in range(len(s)):
            map_s[s[r]]=map_s.get(s[r],0)+1
            while self.check(map_s,map_t):
                if r-l+1<=ans:
                    ret=s[l:r+1]
                    ans=r-l+1
                map_s[s[l]]-=1
                l+=1
        if ans==float('inf'):
            return ""
        else:
            return ret
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        