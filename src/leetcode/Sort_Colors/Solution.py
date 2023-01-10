from typing import List
from collections import Counter


class Solution:
    def sortColors(self, nums: List[int]) -> None:
        counter = Counter(nums)
        idx = 0
        for i in range(3):
            for _ in range(counter[i]):
                nums[idx] = i
                idx += 1
        # This is nothing to do with the answer
        print(nums)


s = Solution()
s.sortColors([2, 0, 2, 1, 1, 0])
