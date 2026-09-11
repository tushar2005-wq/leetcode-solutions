class Solution(object):
    def coinChange(self, coins, amount):
        n=len(coins)
        dp={}
        def solve(idx,amount):
            #base case
            if idx==0:
                if amount%coins[0]==0:
                    return amount//coins[0]
                return float('inf')
            #check for dp value
            if (idx,amount) in dp:
                return dp[(idx,amount)]
            #not taking condition
            not_take=solve(idx-1,amount)
            #taking condition
            take=float('inf')
            if amount>=coins[idx]:
                take=1+solve(idx,amount-coins[idx])
            #putting the value in dp
            dp[(idx,amount)]=min(take,not_take)
            #returning the final value
            return dp[(idx,amount)]
        ans=solve(n-1,amount)
        return -1 if ans==float('inf') else ans

        """
        :type coins: List[int]
        :type amount: int
        :rtype: int
        """
        