# [Majority Element](https://leetcode.com/problems/majority-element/)

> 2020-12-20

주어진 배열의 element 중에 가장 많이 등장한 element를 return 하는 문제입니다.

### solve 1.
`collection.Counter`라이브러리를 사용해서 element들의 수를 dictionary 형태로 저장한 후, 가장 value가 가장 큰 값을 return 합니다.
```python
from collections import Counter


class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        counter = Counter(nums)
        return max(counter, key=lambda x: counter[x])
```
