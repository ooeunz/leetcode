from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if not prices:
            return 0
        end = prices[-1]
        mx = 0
        for i in range(len(prices) - 1, -1, -1):
            mx = max(end - prices[i], mx)
            if prices[i] > end:
                end = prices[i]
        return mx


s = Solution()
print(s.maxProfit([7, 1, 5, 3, 6, 4]) == 5)
print(s.maxProfit([7, 6, 4, 3, 1]) == 0)
print(s.maxProfit([0]) == 0)
