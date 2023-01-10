from typing import List


class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        if nums2:
            for i in range(m):
                if nums1[i] > nums2[0]:
                    nums1[i], nums2[0] = nums2[0], nums1[i]
                    for j in range(n - 1):
                        if nums2[j] > nums2[j + 1]:
                            nums2[j + 1], nums2[j] = nums2[j], nums2[j + 1]
            for i in range(n):
                nums1[m] = nums2[i]
                m += 1


s = Solution()
print(s.merge([1, 2, 3, 0, 0, 0], 3, [2, 5, 6], 3))
