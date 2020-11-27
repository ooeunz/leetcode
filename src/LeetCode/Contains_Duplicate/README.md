# [ContainsDuplicate](https://leetcode.com/explore/interview/card/top-interview-questions-easy/92/array/578/)

> 2020-11-27

집합 자료형 Set을 이용하여 쉽게 풀 수 있는 문제이다. 단순히 자료구조를 이해하고 있는지를 확인하기 위한 문제인 것 같다.

주어진 배열 nums와 중복을 허용하지 않는 `set`의 길이를 비교하여 두 자료구조의 길이가 일치하지 않다면 배열에 중복이 있다고 판단할 수 있다.

```python
class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        return len(nums) != len(set(nums))
```