from typing import List
import collections


class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        pkg = collections.Counter(nums)
        return list(filter(lambda x: pkg[x] == 1, pkg))[0]


s = Solution()
print(s.singleNumber([2,2,1]) == 1)
print(s.singleNumber([4,1,2,1,2]) == 4)
print(s.singleNumber([1]) == 1)