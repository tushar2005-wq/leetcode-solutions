class Solution(object):
    def maxIceCream(self, costs, coins):
        n=len(costs)
        costs=sorted(costs,reverse=False)
        ice_cream=0
        for i in range(n):
            if costs[i]<=coins:
                ice_cream+=1
                coins-=costs[i]
        return ice_cream
        """
        :type costs: List[int]
        :type coins: int
        :rtype: int
        """
        