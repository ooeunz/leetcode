from typing import List


class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        length = len(nums)
        if length == 0:
            return 0
        mx = float('-inf')
        for i in range(length):
            for j in range(i + 1, length + 1):
                mx = max(mx, sum(nums[i:j]))
        return mx


s = Solution()
print(s.maxSubArray([-2, 1, -3, 4, -1, 2, 1, -5, 4]) == 6)
print(s.maxSubArray([1]) == 1)
print(s.maxSubArray([0]) == 0)
print(s.maxSubArray([-1]) == -1)
print(s.maxSubArray([-2147483647]) == -2147483647)
print(s.maxSubArray([-2, 1]) == 1)
print(s.maxSubArray([-2, -1]) == -1)
print(s.maxSubArray([]) == 0)
