class Solution:
    def coinChange(self, coins: list[int], amount: int) -> int:
        # selecting a maximum number as min amount to begin
        min_amount: int = amount + 1
        dp: list[int] = [min_amount]*min_amount
        dp[0] = 0  # we need zero coins to reach 0 amount

        for amt in range(1, min_amount):
            for coin in coins:
                amt_left = amt - coin
                if amt_left >= 0:
                    dp[amt] = min(dp[amt], dp[amt_left]) + 1

        # if dp[amount] == min_amount then we haven't found a change of coins that would lead to "amount"
        return -1 if dp[amount] == min_amount else dp[amount]

solution = Solution()
print(solution.coinChange([1,2,5], 11))