from typing import List
import collections


class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        nums1 = collections.deque(nums1)
        nums2 = collections.deque(nums2)
        ans = []
        while nums1 and nums2:
            if nums1[0] < nums2[0]:
                ans.append(nums1.popleft())
            else:
                ans.append(nums2.popleft())
        ans += nums1 + nums2
        mid = len(ans) // 2
        if len(ans) % 2:
            return ans[mid]
        else:
            return (ans[mid - 1] + ans[mid]) / 2


s = Solution()
print(s.findMedianSortedArrays([1, 3], [2]) == 2)
print(s.findMedianSortedArrays([1, 2], [3, 4]) == 2.5)
print(s.findMedianSortedArrays([0, 0], [0, 0]) == 0)
print(s.findMedianSortedArrays([], [1]) == 1)
print(s.findMedianSortedArrays([2], []) == 2)
