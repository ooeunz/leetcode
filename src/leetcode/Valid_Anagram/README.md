# [Valid Anagram](https://leetcode.com/explore/interview/card/top-interview-questions-easy/127/strings/882/)

> 2020-12-28

주어진 문자열이 Anagram인지를 확인하는 문제입니다.

### solve 1.
Anagram이란 결국 문자의 수만 같으면 성립이 되기 때문에 `collection.Counter()`를 이용해서 두 문자열을 비교합니다.
```python
from collections import Counter


class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        return Counter(s) == Counter(t)
```