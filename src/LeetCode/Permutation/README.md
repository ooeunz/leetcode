# [Permutation](https://leetcode.com/explore/interview/card/top-interview-questions-medium/109/backtracking/795/)

> 2020-12-18

주어진 배열을 이용해서 permutation을 구현하는 문제입니다.

### solve 1.
python에는 permutation을 구현해주는 library가 존재하기 때문에 간단하게 한줄 코드로 구현할 수 있습니다.

```python
from itertools import permutations


class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        return list(map(lambda x: list(x), permutations(nums, len(nums))))
```
