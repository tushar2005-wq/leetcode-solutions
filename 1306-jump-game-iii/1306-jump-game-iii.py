class Solution(object):
    def canReach(self, arr, start):
        visited=set()
        def dfs(i):
            if i>=len(arr) or i<0:
                return False
            if arr[i]==0:
                return True
            if i in visited:
                return False
            visited.add(i)
            return dfs(i+arr[i]) or dfs(i-arr[i])
        return dfs(start)
        """
        :type arr: List[int]
        :type start: int
        :rtype: bool
        """
        