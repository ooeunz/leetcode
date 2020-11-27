from typing import List


class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        a = 0
        for i in nums:
            a ^= i
        return a


s = Solution()
print(s.singleNumber([2, 2, 1]) == 1)
print(s.singleNumber([4, 1, 2, 1, 2]) == 4)
print(s.singleNumber([1]) == 1)
