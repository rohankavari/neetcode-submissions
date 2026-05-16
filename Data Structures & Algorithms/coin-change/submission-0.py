class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        memo = {}
        def f(coins,amount):
            if amount == 0:
                return 0
            if amount < 0:
                return float("inf")
            if amount in memo:
                return memo[amount]
            ans = float("inf")
            for i in coins:
                ans = min(ans, 1 + f(coins, amount - i))
            memo[amount] = ans
            return ans
        r = f(coins,amount)

        if r == float("inf"):
            return -1
        return r