from typing import List


class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        ans = []
        for i in range(len(nums) - 2):
            if i > 0 and nums[i - 1] == nums[i]:
                continue
            left, right = i + 1, len(nums) - 1
            while left < right:
                sum_num = nums[i] + nums[left] + nums[right]
                if sum_num < 0:
                    left += 1
                elif sum_num > 0:
                    right -= 1
                else:
                    ans.append([nums[i], nums[left], nums[right]])
                    while left < len(nums) - 1 and nums[left + 1] == nums[left]:
                        left += 1
                    while right > 0 and nums[right - 1] == nums[right]:
                        right -= 1
                    left += 1
                    right -= 1
        return ans


s = Solution()
print(s.threeSum([-1, 0, 1, 2, -1, -4]))
print(s.threeSum([-1, 0, 1]))
