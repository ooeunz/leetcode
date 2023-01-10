from typing import List


class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        ans = []
        used = [False] * len(nums)

        def generate(chosen, used):
            if len(chosen) == len(nums):
                ans.append(chosen[:])
                return
            for i in range(len(nums)):
                if not used[i]:
                    chosen.append(nums[i])
                    used[i] = True
                    generate(chosen, used)
                    used[i] = False
                    chosen.pop()
        generate([], used)
        return ans


s = Solution()
print(s.permute([1, 2, 3]))
print(s.permute([0, 1]))
