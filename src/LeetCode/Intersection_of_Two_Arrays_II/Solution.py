from typing import List
from collections import Counter


class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        ans = []
        cnt = Counter(nums1)
        for num in nums2:
            if num in cnt and cnt[num] > 0:
                ans.append(num)
                cnt[num] -= 1
        return ans


s = Solution()
print(s.intersect([1, 2, 2, 1], [2, 2]) == [2, 2])
print(s.intersect([4, 9, 5], [9, 4, 9, 8, 4]) == [9, 4])
