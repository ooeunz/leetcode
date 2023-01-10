from typing import List


class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0
        ans = nums[0]
        sub_sum = 0
        for num in nums:
            sub_sum += num
            ans = max(ans, sub_sum)
            if sub_sum < 0:
                sub_sum = 0
        return ans


s = Solution()
print(s.maxSubArray([-2, 1, -3, 4, -1, 2, 1, -5, 4]) == 6)
print(s.maxSubArray([1]) == 1)
print(s.maxSubArray([0]) == 0)
print(s.maxSubArray([-1]) == -1)
print(s.maxSubArray([-2147483647]) == -2147483647)
print(s.maxSubArray([-2, 1]) == 1)
print(s.maxSubArray([-2, -1]) == -1)
print(s.maxSubArray([]) == 0)
