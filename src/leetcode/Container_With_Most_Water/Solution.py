from typing import List


class Solution:
    def maxArea(self, height: List[int]) -> int:
        start, end = 0, len(height) - 1
        mx = float('-inf')
        while start < end:
            mx = max(mx, min(height[start], height[end]) * abs(end - start))
            if height[start] < height[end]:
                start += 1
            else:
                end -= 1
        return mx


s = Solution()
print(s.maxArea([1, 1]))
print(s.maxArea([1, 2, 1]))
print(s.maxArea([1, 8, 6, 2, 5, 4, 8, 3, 7]))
print(s.maxArea([4, 3, 2, 1, 4]))
