from typing import List
from collections import Counter


class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        counter = Counter(nums)
        return max(counter, key=lambda x: counter[x])


s = Solution()
print(s.majorityElement([3, 2, 3]) == 3)
print(s.majorityElement([2, 2, 1, 1, 1, 2, 2]) == 2)
