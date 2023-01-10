from typing import List
import collections


class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        if amount == 0:
            return 0
        dp = collections.defaultdict(lambda: float('inf'))
        for i in range(1, amount + 1):
            for coin in coins:
                if coin <= amount and dp[coin] == float('inf'):
                    dp[coin] = 1

                prev_coin = i - coin
                if 0 < prev_coin < float('inf'):
                    dp[i] = min(dp[prev_coin] + 1, dp[i])
        return dp[amount] if dp[amount] < float('inf') else -1


s = Solution()
print(s.coinChange([1, 2, 5], 11) == 3)
print(s.coinChange([2], 3) == -1)
print(s.coinChange([1], 0) == 0)
print(s.coinChange([1], 1) == 1)
print(s.coinChange([1], 2) == 2)
print(s.coinChange([2], 1) == -1)
print(s.coinChange([2147483647], 2) == -1)
print(s.coinChange([1, 2147483647], 2) == 2)
print(s.coinChange([186, 419, 83, 408], 6249) == 20)
