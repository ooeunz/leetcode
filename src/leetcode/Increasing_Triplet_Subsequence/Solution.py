from typing import List


class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:
        if len(nums) < 3:
            return False
        fir, sec = nums[0], float('inf')
        for num in nums:
            if num > sec:
                print(f"fir: {fir}, sec: {sec}, num: {num}")
                return True
            elif num > fir:
                sec = num
            elif num < fir:
                fir = num
        return False


s = Solution()
print(s.increasingTriplet([1, 2, 3, 4, 5]))
print(s.increasingTriplet([5, 4, 3, 2, 1]))
print(s.increasingTriplet([4, 5, 3, 1, 7]))
