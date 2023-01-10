from typing import List


class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        dp = [1] * len(nums)
        mx = 1
        for i in range(len(nums)):
            for j in range(i):
                if nums[j] < nums[i]:
                    dp[i] = max(dp[j] + 1, dp[i])
                    mx = max(mx, dp[i])
        return mx


s = Solution()
print(s.lengthOfLIS([10, 9, 2, 5, 3, 7, 101, 18]) == 4)
print(s.lengthOfLIS([0, 1, 0, 3, 2, 3]) == 4)
print(s.lengthOfLIS([7, 7, 7, 7, 7, 7, 7]) == 1)
