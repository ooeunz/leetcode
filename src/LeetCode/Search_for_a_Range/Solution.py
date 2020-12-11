from typing import List


class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        if not nums:
            return [-1, -1]
        start = -1
        for i in range(len(nums)):
            if nums[i] == target:
                start = i
                break
        for end in range(len(nums) - 1, start, -1):
            if nums[end] == target:
                return [start, end]
        return [-1, -1]


s = Solution()
print(s.searchRange([5, 7, 7, 8, 8, 10], 8) == [3, 4])
print(s.searchRange([5, 7, 7, 8, 8, 10], 6) == [-1, -1])
print(s.searchRange([], 0) == [-1, -1])
