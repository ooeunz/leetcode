from typing import List


class Solution:
    def reverse(self, nums: list, start: int, end: int):
        while start < end:
            nums[start], nums[end] = nums[end], nums[start]
            start += 1
            end -= 1

    def rotate(self, nums: List[int], k: int) -> None:
        n = len(nums)
        k %= n

        self.reverse(nums, 0, n - 1)
        self.reverse(nums, 0, k - 1)
        self.reverse(nums, k, n - 1)
        # This is nothing to do with the answer
        print(nums)


s = Solution()
s.rotate([1, 2, 3, 4, 5, 6, 7], 3)
