from typing import List
from collections import Counter


class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        counter = Counter(nums)
        return list(filter(lambda x: counter[x] > 1, counter))[0]


s = Solution()
print(s.findDuplicate([1, 3, 4, 2, 2]))
