from typing import List


class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        mn = [nums[0]] + [0 for _ in range(1, len(nums))]
        mx = [nums[0]] + [0 for _ in range(1, len(nums))]

        for i in range(1, len(nums)):
            cur = nums[i]
            mn[i] = min(cur, mn[i - 1] * cur, mx[i - 1] * cur)
            mx[i] = max(cur, mn[i - 1] * cur, mx[i - 1] * cur)
        return max(mx)


s = Solution()
print(s.maxProduct([2, 3, -2, 4]))
print(s.maxProduct([-2, 0, -1]))
