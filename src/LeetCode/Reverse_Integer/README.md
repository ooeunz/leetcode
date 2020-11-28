# [Reverse Integer](https://leetcode.com/explore/interview/card/top-interview-questions-easy/127/strings/880/)

> 2020-11-28

정수를 뒤집는 문제입니다. 음수일 경우와 양수일 경우를 다르게 고려해야한다는 점과, 2의 31승을 넘어가면 0을 반환해야한다는 예외를 주의해서 풀어야합니다.

### solve 1.
정수를 문자열로 바꾼 후 뒤집고 다시 정수 형태로 변경합니다.
이때, 2의 31승을 넘어가는 값이면 0을 반환해줍니다.

```python
class Solution:
    def reverse(self, x: int) -> int:
        if x < 0:
            ans = -int(''.join(list(reversed(str(abs(x))))))
            return 0 if ans < -2 ** 31 else ans
        else:
            ans = int(''.join(list(reversed(str(x)))))
            return 0 if ans > 2 ** 31 else ans
```