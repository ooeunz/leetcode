# [Kth Largest Element in an Array](https://leetcode.com/explore/interview/card/top-interview-questions-medium/110/sorting-and-searching/800/)

> 2020-12-11

정렬되지 않은 배열이 있을 때, `k`번째로 큰 수를 반환하는 문제입니다.

### solve 1.
주어진 배열을 정렬한 후 `k - 1`번째 (배열을 0부터 시작하므로) element를 반환합니다.
time complexity는 `O(n log n)`입니다.

```python
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        return sorted(nums, reverse=True)[k - 1]
```