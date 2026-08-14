class Solution(object):
    def check(self,map_s):
        count=0
        for i in map_s:
            if map_s[i]>2:
                count+=1
        return count==0
    def maximumLengthSubstring(self, s):
        l=0
        ans=0
        map_s={}
        for r in range(len(s)):
            map_s[s[r]]=map_s.get(s[r],0)+1
            while not self.check(map_s):
                map_s[s[l]]-=1
                l+=1
            ans=max(ans,r-l+1)
        return ans
        """
        :type s: str
        :rtype: int
        """
        