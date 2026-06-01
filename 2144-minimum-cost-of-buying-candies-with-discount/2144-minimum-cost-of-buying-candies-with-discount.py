class Solution(object):
    def minimumCost(self, cost):
        sum_=0
        cost.sort(reverse=True)
        for i in range(len(cost)):
            if i % 3 != 2:      # every 3rd candy is free
                sum_ += cost[i]

        return sum_
        """
        :type cost: List[int]
        :rtype: int
        """
        