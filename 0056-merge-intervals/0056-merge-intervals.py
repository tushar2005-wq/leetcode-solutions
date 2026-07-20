class Solution(object):
    def merge(self, intervals):
        intervals.sort(key=lambda x:x[0])
        res=[intervals[0]]
        for i in range(1,len(intervals)):
            last=res[-1]
            curr=intervals[i]
            if curr[0]<=last[1]:
                last[1]=max(curr[1],last[1])
            else:
                res.append(curr)
        return res

        """
        :type intervals: List[List[int]]
        :rtype: List[List[int]]
        """
        