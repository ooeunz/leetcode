# [Median_of_Two_Sorted_Arrays](https://leetcode.com/problems/median-of-two-sorted-arrays/)

> 2020-11-08

정렬과 관련된 문제입니다. 난이도는 **Hard**이지만 정렬 알고리즘에 대한 이해도가 있다면 쉽게 풀 수 있는 문제입니다.

### solve 1.
문제에서 **정렬이 된 문자열 2개**를 주기 때문에 merge sort의 마지막 단계, 즉 정렬이 된 두 문자열을 합치는 부분만 구현 함으로써 문제를 풀 수 있습니다.
```python
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
```