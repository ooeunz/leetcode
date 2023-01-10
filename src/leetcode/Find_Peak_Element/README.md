# [Find Peak Element](https://leetcode.com/explore/interview/card/top-interview-questions-medium/110/sorting-and-searching/801/)

> 2020-12-11

주어진 배열에서 가장 값이 큰 element의 index값을 반환하는 문제입니다.

### solve 1.
`enumerate`와 `max`라이브러리를 적절히 사용해서 `O(n)`만큼의 time complexity로 문제를 해결합니다.

```python
class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        idx, val = max(enumerate(nums), key=lambda x: x[1])
        return idx
```