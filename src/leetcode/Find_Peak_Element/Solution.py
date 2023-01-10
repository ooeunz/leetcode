from typing import List


class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        idx, val = max(enumerate(nums), key=lambda x: x[1])
        return idx


s = Solution()
print(s.findPeakElement([1, 2, 3, 1]) == 2)
print(s.findPeakElement([1, 2, 1, 3, 5, 6, 4]) == 5)
