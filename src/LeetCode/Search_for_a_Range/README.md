# [Search for a Range](https://leetcode.com/explore/interview/card/top-interview-questions-medium/110/sorting-and-searching/802/)

> 2020-12-11

정렬된 배열이 주어졌을 때 `target`이 있는 가장 첫번째 index와 가장 마지막 index를 return하는 문제입니다.
만약 target이 존재하지 않을 경우 `[-1, -1]`을 return 합니다.

### solve 1.
알고리즘의 핵심적인 아이디어는 배열이 정렬되어 있다는 것을 이용하는 것입니다.
배열의 첫번째 index부터 `target`을 찾다가 만약 target을 찾으면 해당 index를 `start`로 삼습니다. 
다시 배열의 끝에서부터 `start`까지 앞으로 하나씩 검사하며 `target`을 찾으면 해당 index를 `end`로 삼고 return 합니다.

```python
class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        if not nums:
            return [-1, -1]
        start = -1
        for i in range(len(nums)):
            if nums[i] == target:
                start = i
                break
        for end in range(len(nums) - 1, start, -1):
            if nums[end] == target:
                return [start, end]
        return [-1, -1]
```