# [Multiply Strings](https://leetcode.com/problems/multiply-strings/)

> 2020-01-10

문자열로 주어지는 두 수를 곱한 값을 return하는 문제입니다.

> 왜 medium 난이도인지 모르겠습니다...

### solve 1.
두 수를 정수타입으로 캐스팅 한 후에 연산 후 다시 문자열로 캐스팅하여 return합니다.

```python
class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        return str(int(num1) * int(num2))
```