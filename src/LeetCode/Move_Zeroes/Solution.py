from typing import List


class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        cnt = 0
        pos = 0
        for idx, val in enumerate(nums):
            if val == 0:
                cnt += 1
            else:
                nums[pos] = val
                pos += 1
        length = len(nums) - 1
        for i in range(length, length - cnt, -1):
            nums[i] = 0

        # This is nothing to do with the answer
        print(nums)


s = Solution()
print(s.moveZeroes([0, 1, 0, 3, 12]))
