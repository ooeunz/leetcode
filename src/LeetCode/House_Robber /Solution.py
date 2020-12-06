from typing import List


class Solution:
    def find_rich_house(self, idx: int, val: int, nums: list):
        if idx >= len(nums):
            return val
        current_val = val + nums[idx]
        return max(
            self.find_rich_house(idx + 2, current_val, nums),
            self.find_rich_house(idx + 3, current_val, nums)
        )

    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        return max(
            self.find_rich_house(0, 0, nums),
            self.find_rich_house(1, 0, nums)
        )


s = Solution()
print(s.rob([]) == 0)
print(s.rob([1, 2, 1, 1]) == 3)
print(s.rob([4, 1, 2, 7, 5, 3, 1]) == 14)
print(s.rob([1, 2, 3, 1]) == 4)
print(s.rob([2, 7, 9, 3, 1]) == 12)
