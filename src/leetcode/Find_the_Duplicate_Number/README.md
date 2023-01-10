# [Find the Duplicate Number](https://leetcode.com/problems/find-the-duplicate-number/)

> 2020-01-10

정수로 이루어진 배열 `nums`가 주어졌을때, 배열안에 중복된 정수를 출련하는 문제입니다.

### solve 1.
배열 안에 수를 dictionary 형태로 저장하는 `collection.Counter` 라이브러리를 이용해서 주어진 배열을 Counter 형태로 변환한 다음, 값이 1이상인 key를 return 합니다.
해당 알고리즘의 경우 time complexity는 O(n)이 됩니다.
 
```python
from collections import Counter


class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        counter = Counter(nums)
        return list(filter(lambda x: counter[x] > 1, counter))[0]
```