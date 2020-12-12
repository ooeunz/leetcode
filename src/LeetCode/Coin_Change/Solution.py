from typing import List
import collections


class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        if amount < 0:
            return 0
        dp = collections.defaultdict(lambda: float('inf'))
        ans = self.coin_change(coins, amount, dp)
        return ans

    def coin_change(self, coins: list, amount: int, dp):
        if amount < 0:
            return -1
        if amount == 0:
            return 0
        if amount - 1 in dp:
            return dp[amount - 1]
        mn = float('inf')
        for coin in coins:
            res = self.coin_change(coins, amount - coin, dp)
            if 0 <= res < mn:
                mn = res + 1
        dp[amount - 1] = mn if mn != float('inf') else -1
        return dp[amount - 1]


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
