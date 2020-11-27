# [Single Number](https://leetcode.com/explore/interview/card/top-interview-questions-easy/92/array/549/)

> 2020-11-27

배열 안에 중복되지 않은 수가 있는지 확인하는 문제입니다.

### solve 1.
이 문제 역시 딕셔너리를 활용한 라이브러리인 `collection.Couter`를 이용하여 쉽게 풀 수 있습니다.
`collection.Couter`는 배열 안에 각 요소가 몇개씩 존재하는지 딕셔너리 형태로 만들어주는 라이브러리입니다.
해당 라이브러리를 이용해 딕셔너리를 만든 후 value값이 1인 element를 `filter`를 이용해서 찾아냅니다.
```python
import collections


class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        pkg = collections.Counter(nums)
        return list(filter(lambda x: pkg[x] == 1, pkg))[0]
```
