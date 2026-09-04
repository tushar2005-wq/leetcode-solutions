class Solution:
    def numSquares(self, n):

        # Perfect squares
        squares = []
        i = 1

        while i * i <= n:
            squares.append(i * i)
            i += 1

        m = len(squares)

        # memo[index][target]
        memo = [[-1] * (n + 1) for _ in range(m)]

        def solve(index, target):

            if target == 0:
                return 0

            if index < 0:
                return float('inf')

            if memo[index][target] != -1:
                return memo[index][target]

            # Not take
            not_take = solve(index - 1, target)

            # Take
            take = float('inf')

            if squares[index] <= target:
                take = 1 + solve(index, target - squares[index])

            memo[index][target] = min(take, not_take)

            return memo[index][target]

        return solve(m - 1, n)