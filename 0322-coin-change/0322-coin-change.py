class Solution(object):
    def coinChange(self, coins, amount):
        n=len(coins)
        dp={}
        def solve(idx,amount):
            if idx==0:
                if amount%coins[0]==0:
                    return amount // coins[0]
                return float('inf')
            if (idx,amount) in dp:
                return dp[(idx,amount)]
            not_take=solve(idx-1,amount)
            take=float('inf')
            if coins[idx]<=amount:
                take=1+solve(idx,amount-coins[idx])
            dp[(idx,amount)]=min(take,not_take)
            return dp[(idx,amount)]
        ans=solve(n-1,amount)
        return -1 if ans==float('inf') else ans

        """
        :type coins: List[int]
        :type amount: int
        :rtype: int
        """
        