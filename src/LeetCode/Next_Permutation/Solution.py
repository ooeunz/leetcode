from typing import List
from itertools import permutations


class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        if len(nums) == 1:
            return
        permu = sorted(list(set(permutations(nums, len(nums)))))
        start, end = 0, len(permu)

        def change(nums, per):
            for i in range(len(nums)):
                nums[i] = per[i]

        while start < end:
            mid = (start + end) // 2
            if permu[mid] == tuple(nums):
                if mid + 1 >= len(permu):
                    change(nums, permu[0])
                else:
                    change(nums, permu[mid + 1])
                break
            elif permu[mid] > tuple(nums):
                end = mid
            else:
                start = mid


s = Solution()
s.nextPermutation([1, 2, 3])
s.nextPermutation([5, 1, 1])
s.nextPermutation([3, 2, 1])
s.nextPermutation([1, 1, 5])
s.nextPermutation([1, 3, 2])
s.nextPermutation([1])
