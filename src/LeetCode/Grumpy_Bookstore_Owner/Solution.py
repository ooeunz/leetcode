from typing import List


class Solution:
    def maxSatisfied(self, customers: List[int], grumpy: List[int], X: int) -> int:
        ans = standard = 0
        for c, g in zip(customers, grumpy):
            if not g:
                standard += c

        start = 0
        while start < len(customers) - X + 1:
            tmp = 0
            for i in range(start, start + X):
                if grumpy[i]:
                    tmp += customers[i]

            ans = max(ans, standard + tmp)
            start += 1
            while len(grumpy) > start and grumpy[start] != 1 and start < len(customers) - X:
                start += 1
        return ans


s = Solution()
print(s.maxSatisfied([1, 0, 1, 2, 1, 1, 7, 5], [0, 1, 0, 1, 0, 1, 0, 1], 3) == 16)
print(s.maxSatisfied([6, 10, 2, 1, 7, 9], [1, 0, 0, 0, 0, 1], 3) == 29)
