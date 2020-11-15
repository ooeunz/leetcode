from typing import List


class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0
        ans = 0
        index = 1
        for i in range(1, len(nums)):
            if nums[i - 1] != nums[i]:
                nums[index] = nums[i]
                ans += 1
                index += 1
        return ans + 1


s = Solution()
print(s.removeDuplicates([1, 1, 2]) == 2)
print(s.removeDuplicates([0, 0, 1, 1, 1, 2, 2, 3, 3, 4]) == 5)
