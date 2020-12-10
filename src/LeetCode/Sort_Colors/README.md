# [Sort Colors](https://leetcode.com/explore/interview/card/top-interview-questions-medium/110/sorting-and-searching/798/)

> 2020-12-11

`0`, `1`, `2`가 배열안에 정렬되지 않은채로 주어졌을 때, `[0, 0, 0, 1, 1, 2, 2]`와 같은 형태로 추가적인 메모리를 할당하지 않고 정렬하는 알고리즘을 짜는 문제입니다.

### solve 1.
주어진 수가 `0`, `1`, `2` 3가지 밖에 없으므로 `Counter` 라이브러리를 사용해서 각 element들의 수를 저장합니다.
그리고 0부터 2까지 하나씩 수를 검사하며 그 수만큼 `nums` 배열에 차례대로 채워줍니다.

`Counter`는 모든 배열의 element들을 필수적으로 체크해야하기 때문에 `O(n)`만큼의 time complexity가 필요합니다.
또한 아래의 알고리즘은 `O(3n)`만큼이 소요되기 때문에 토탈 `O(4n)`만큼의 time complexity가 요구됩니다.

하지만 Big O표기법은 상수를 제외하므로 최종적으로 `O(n)`이 됩니다.

```python
class Solution:
    def sortColors(self, nums: List[int]) -> None:
        counter = Counter(nums)
        idx = 0
        for i in range(3):
            for _ in range(counter[i]):
                nums[idx] = i
                idx += 1
```