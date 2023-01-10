from typing import List


class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        cnt = 0
        pos = 0
        for num in nums:
            if num == 0:
                cnt += 1
            else:
                nums[pos] = num
                pos += 1
        while cnt > 0:
            nums[len(nums) - cnt] = 0
            cnt -= 1

        # This is nothing to do with the answer
        print(nums)


s = Solution()
print(s.moveZeroes([0, 1, 0, 3, 12]))
