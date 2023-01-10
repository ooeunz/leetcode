from typing import List


class Solution:
    def maxSatisfied(self, customers: List[int], grumpy: List[int], X: int) -> int:
        ans = 0
        for i in range(len(grumpy)):
            if grumpy[i] == 0:
                ans += customers[i]
                customers[i] = 0
        best_solution = 0
        cur = 0
        for i, customer in enumerate(customers):
            cur += customer
            if i >= X:
                cur -= customers[i - X]
            best_solution = max(best_solution, cur)
        return ans + best_solution


s = Solution()
print(s.maxSatisfied([1, 0, 1, 2, 1, 1, 7, 5], [0, 1, 0, 1, 0, 1, 0, 1], 3) == 16)
print(s.maxSatisfied([6, 10, 2, 1, 7, 9], [1, 0, 0, 0, 0, 1], 3) == 29)
