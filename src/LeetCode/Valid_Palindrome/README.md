# [Valid Palindrome](https://leetcode.com/explore/interview/card/top-interview-questions-easy/127/strings/883/)

> 2020-11-28

주어진 문자열이 영문자(대소문자 구별 없이) 및 숫자만을 유효하다는 가정 했을 경우 palindrome인지 확인하는 문제입니다.

### solve 1.
풀이의 핵심은 주어진 문자열이 숫자 또는 영문자로만 이루어진 pure한 문자열로 변환하는 것입니다.
그를 위해 문자열을 ASCII로 변환하여 정수의 범위와 소문자 범위 안에 들어가는 문자만을 선택적으로 `ss`문자열에 넣은 후, `reversed`하여 두 문자열을 비교합니다. 
```python
class Solution:
    def isPalindrome(self, s: str) -> bool:
        ss = ""
        for char in s.replace(" ", "").lower():
            if 48 <= ord(char) <= 57 or 97 <= ord(char) <= 122:
                ss += char
        return ss == "".join(list(reversed(ss)))
```