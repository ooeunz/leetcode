from typing import List


class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        for i in range(k):
            previous = nums[-1]
            for j in range(len(nums)):
                nums[j], previous = previous, nums[j]
        # This is nothing to do with the answer.
        print(nums)


s = Solution()
s.rotate([1, 2, 3, 4, 5, 6, 7], 3)
