from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        have = []
        ans = 0
        for i in range(len(prices) - 1):
            current = prices[i]
            future = prices[i + 1]
            if not have and current < future:
                have.append(current)
            elif have and current > future:
                ans += current - have.pop()
        if have:
            last_day = prices[-1]
            ans += last_day - have.pop()
        return ans


s = Solution()
print(s.maxProfit([7, 1, 5, 3, 6, 4]) == 7)
print(s.maxProfit([1, 2, 3, 4, 5]) == 4)
print(s.maxProfit([7, 6, 4, 3, 1]) == 0)
print(s.maxProfit([6, 1, 3, 2, 4, 7]) == 7)
