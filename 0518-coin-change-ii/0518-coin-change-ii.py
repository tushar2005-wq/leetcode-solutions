class Solution(object):
    def change(self, amount, coins):
        if not coins:
            return 0
        n=len(coins)
        dp={}
        def solve(idx,amount):
            if amount==0:
                return 1
            if idx==0:
                return 1 if amount%coins[0]==0 else 0
            if (idx,amount) in dp:
                return dp[(idx,amount)]
            not_take=solve(idx-1,amount)
            take=0
            if amount>=coins[idx]:
                take=solve(idx,amount-coins[idx])
            dp[(idx,amount)]=take+not_take
            return dp[(idx,amount)]
        ans=solve(n-1,amount)
        return ans
        """
        :type amount: int
        :type coins: List[int]
        :rtype: int
        """
        