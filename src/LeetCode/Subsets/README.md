# [Subsets](https://leetcode.com/explore/interview/card/top-interview-questions-medium/109/backtracking/796/)

> 2020-12-18

배열이 주어 졌을 때, 배열의 각 element들을 이용한 combination을 만드는 문제입니다.

### solve 1.
이 문제는 `itertools.combination`를 이용해서 간단하게 풀 수 있습니다.
`nums`의 element들을 이용해서 `nums`의 길이만큼 combination을 모두 구해서 `ans` 배열에 추가합니다.
 
```python
from itertools import combinations


class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        ans = []
        for i in range(len(nums) + 1):
            ans += list(map(lambda x: list(x), combinations(nums, i)))
```

### solve 2.
두번 째 방법은 `itertools.combination`을 직접 구현해서 문제를 푸는 방식입니다.
먼저 combination을 담은 `ans`을 선언합니다.

그 다음 실제로 combination을 구현하는 `generate` 함수를 선언해줍니다.
정해진 길이만큼의 combination을 구하는 것이 아니라 모든 길이만큼 combination을 구해야하기 때문에 `generate`가 실행될 때마다 `ans`에 값을 추가합니다.
그리고 만약 현재 만들고 있는 combination의 길이 즉 `chosen`의 길이가 `nums`의 길이가 같다면 모든 element를 사용했다는 뜻이기 때문에 return 합니다.

combination은 permutation과 다르게 순서를 고려하지 않고 각 element의 **조합**만을 고려하기 때문에 `start` 값을 지정해주어야 합니다.
만약 `chosen`의 값이 비어있다면 `0`부터 시작하고, 그렇지 않다면 `chosen`의 마지막 index 다음부터 for문을 돌리도록 합니다.

for문을 탈출하면 `ans` 값을 return 하도록합니다.

```python
class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        ans = []

        def generate(chosen):
            ans.append(chosen[:])
            if len(chosen) == len(nums):
                return
            start = nums.index(chosen[-1]) + 1 if chosen else 0
            for nxt in range(start, len(nums)):
                chosen.append(nums[nxt])
                generate(chosen)
                chosen.pop()
        generate([])
        return ans
```
