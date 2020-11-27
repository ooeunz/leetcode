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

### solve 2.
> Follow up: Could you implement a solution with a linear runtime complexity and without using extra memory?

Follow up으로 한번의 loop와 extra memory 없이 정답을 리턴하는 알고리즘이 존재합니다. 바로 **비트 연산 XOR**을 이용하는 것 입니다.
XOR은 두 값이 일치하지 않을 때 True를 반환하는 연산입니다. 그리고 특히나 **결합 법칙**이 성립하기 때문에 `(x (+) y) (+) z = x (+) (y (+) z)`와 같은 식 역시 성립됩니다.
따라서 하나의 변수에 모두 `^=` 비트 연산을 하여 가장 마지막에 남은 `False`로 return되는 값을 확인할 수 있습니다.
```python
class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        a = 0
        for i in nums:
            a ^= i
        return a
```