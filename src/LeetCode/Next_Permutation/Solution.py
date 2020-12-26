from typing import List


class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        decrease_section = next_large = len(nums) - 1
        while decrease_section > 0 and nums[decrease_section - 1] >= nums[decrease_section]:
            decrease_section -= 1
        if decrease_section == 0:
            nums.reverse()
            return

        pivot = decrease_section - 1
        while nums[pivot] >= nums[next_large]:
            next_large -= 1
        nums[pivot], nums[next_large] = nums[next_large], nums[pivot]

        def reverse_lst(lst: list, start, end):
            while start < end:
                lst[start], lst[end] = lst[end], lst[start]
                start += 1
                end -= 1
        reverse_lst(nums, pivot + 1, len(nums) - 1)
        # This is nothing to do with the answer
        print(nums)


s = Solution()
s.nextPermutation([1, 2, 3])
# s.nextPermutation([5, 1, 1])
# s.nextPermutation([3, 2, 1])
# s.nextPermutation([1, 1, 5])
# s.nextPermutation([1, 3, 2])
# s.nextPermutation([1])
