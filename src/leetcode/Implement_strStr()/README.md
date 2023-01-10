# [Implement strStr()](https://leetcode.com/explore/interview/card/top-interview-questions-easy/127/strings/885/)

> 2020-11-29

주어진 `haystack` 문자열 중 `needle`문자열이 포함되어 있는지를 확인하는 문제입니다.
만약 포함되어 있다면 시작점 index 값을 return하고, 그렇지 않다 -1을 return합니다.

### solve 1.
이 문제를 푸는 가장 쉬운 방법은 python 내장 라이브러리인 `.startswith()`를 이용하는 방법입니다.
먼저 `haystack`과 `needle`의 길이가 같다면 0을 return하도록 합니다. 여기에는 불필요하게 연산을 하는 것을 줄여주는 목적도 있지만,
두 문자열이 `""`일 경우 for문을 돌지 않는 것을 방지하기 위함도 있습니다.

그런 다음 for문을 돌며 `haystack`의 문자의 위치를 하나씩 타겟으로 `.startswith()`를 이용해 `needle`이 해당 문자열에 포함되어 있는지를 확인합니다.
```python
class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        if haystack == needle:
            return 0
        for i in range(len(haystack)):
            if haystack[i:].startswith(needle):
                return i
        return -1
```