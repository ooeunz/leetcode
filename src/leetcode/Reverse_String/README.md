# [Reverse String](https://leetcode.com/explore/interview/card/top-interview-questions-easy/127/strings/879/)

> 2020-11-28

문자열을 거꾸로 뒤집는 문제입니다.

### solve 1.
배열의 시작점을 `start`로, 끝을 `end`로 지정한 다음 서로를 향해서 한칸씩 당겨오며 위치를 변경해줍니다.
```python
class Solution:
    def reverseString(self, s: List[str]) -> None:
        start, end = 0, len(s) - 1
        while start < end:
            s[start], s[end] = s[end], s[start]
            start, end = start + 1, end - 1
```