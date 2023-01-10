# [Search in Rotated Sorted Array](https://leetcode.com/explore/interview/card/top-interview-questions-medium/110/sorting-and-searching/804/)

> 2020-12-11

정렬된 정수로 이루어진 배열이 있을 때, 옆으로 ratate 되었을 경우 `target`이 몇번째 index에 있는지 찾는 문제입니다.

### solve 1.
rotate를 신경쓰지 않고 처음부터 탐색하여 `target`을 발견하면 해당 index를 return 해줍니다.
one path 탐색을 하기 때문에 time complexity는 `O(n)`입니다.

```python
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        for i in range(len(nums)):
            if nums[i] == target:
                return i
        return -1
```