from typing import List


class Solution:
    def canJump(self, nums: List[int]) -> bool:
        dp = [nums[0]] + [0] * (len(nums) - 1)
        for i in range(1, len(nums)):
            if dp[i - 1]:
                dp[i] = max(dp[i - 1] - 1, nums[i])
            else:
                return False
        return True


s = Solution()
print(s.canJump([2, 3, 1, 1, 4]) is True)
print(s.canJump([3, 2, 1, 0, 4]) is False)
