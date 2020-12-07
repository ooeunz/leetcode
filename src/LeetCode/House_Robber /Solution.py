from typing import List


class Solution:
    def rob(self, nums: List[int]) -> int:
        length = len(nums)
        if length == 0:
            return 0
        if length == 1:
            return nums[0]
        if length == 2:
            return max(nums)

        dp = [0] * length
        dp[0] = nums[0]
        dp[1] = max(nums[0], nums[1])

        for i in range(2, length):
            dp[i] = max(dp[i - 2] + nums[i], dp[i - 1])
        return dp[-1]


s = Solution()
print(s.rob([]) == 0)
print(s.rob([1, 2, 1, 1]) == 3)
print(s.rob([4, 1, 2, 7, 5, 3, 1]) == 14)
print(s.rob([1, 2, 3, 1]) == 4)
print(s.rob([2, 7, 9, 3, 1]) == 12)
