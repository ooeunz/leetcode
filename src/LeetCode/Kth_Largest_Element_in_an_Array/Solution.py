from typing import List


class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        return sorted(nums, reverse=True)[k - 1]


s = Solution()
print(s.findKthLargest([3, 2, 1, 5, 6, 4], 2))
print(s.findKthLargest([3, 2, 3, 1, 2, 4, 5, 5, 6], 4))
