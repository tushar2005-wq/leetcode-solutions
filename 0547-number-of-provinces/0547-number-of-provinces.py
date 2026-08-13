class Solution(object):
    def findCircleNum(self, isConnected):
        n=len(isConnected)
        visited=[False]*n
        count=0
        def dfs(city):
            for neighbour in range(n):
                if isConnected[city][neighbour]==1 and not visited[neighbour]:
                    visited[neighbour]=True
                    dfs(neighbour)
        for city in range(n):
            if not visited[city]:
                visited[city]=True
                dfs(city)
                count+=1
        return count
        """
        :type isConnected: List[List[int]]
        :rtype: int
        """
        