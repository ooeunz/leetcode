# [First Unique Character in a String](https://leetcode.com/explore/interview/card/top-interview-questions-easy/127/strings/881/)

> 2020-11-28

문자열 중 하나만 존재하는 가장 첫번째 문자의 index 값을 return하는 문제입니다.
`collection.Counter()` 라이브러리를 사용해서 각 문자열의 element들의 수를 dictionary 형태로 기록한 후 문자열을 순회합니다.

순회 중 하나만 존재하는 문자를 찾으면 해당 문자의 index 값을 return 합니다.
```python
from collections import Counter


class Solution:
    def firstUniqChar(self, s: str) -> int:
        cnt = Counter(list(s))
        for idx, val in enumerate(s):
            if cnt[val] == 1:
                return idx
        return -1
```