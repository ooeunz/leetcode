from typing import List


class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        ans = []

        def generate(chosen):
            ans.append(chosen[:])
            if len(chosen) == len(nums):
                return
            start = nums.index(chosen[-1]) + 1 if chosen else 0
            for nxt in range(start, len(nums)):
                chosen.append(nums[nxt])
                generate(chosen)
                chosen.pop()
        generate([])
        return ans


s = Solution()
print(s.subsets([1, 2, 3]))