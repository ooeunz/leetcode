from typing import List
from itertools import permutations


class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        return list(map(lambda x: list(x), permutations(nums, len(nums))))


s = Solution()
print(s.permute([1, 2, 3]))
print(s.permute([0, 1]))
