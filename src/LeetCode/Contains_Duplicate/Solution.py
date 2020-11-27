from typing import List


class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        return len(nums) != len(set(nums))


s = Solution()
print(s.containsDuplicate([1, 2, 3, 1]) == True)
print(s.containsDuplicate([1, 2, 3, 4]) == False)
print(s.containsDuplicate([1, 1, 1, 3, 3, 4, 3, 2, 4, 2]) == True)
