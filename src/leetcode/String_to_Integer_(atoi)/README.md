# [String to Integer (atoi)](https://leetcode.com/explore/interview/card/top-interview-questions-easy/127/strings/884/)

> 2020-11-29

문제의 조건은
- 왼쪽의 문자열이 공백으로 시작되는 경우는 무시합니다.
- `-`혹은 `+`로 시작하는 경우는 operator를 반영합니다.
- 문자('.' 포)로 시작하면 0을 return 합니다.
- 숫자로 시작하다가 문자가 나타나면 숫자 부분만 반환합니다.
- 32-bit signed integer의 범위를 넘어가면 32-bit integer의 최대 혹은 최소값을 반환합니다.

> 문제 자체가 알고리즘 보다는 다양한 예외사항을 걸러내는 구현 자체에 초점이 맞춰져 있어서 좋은 문제로 여겨지지는 않습니다.

### solve 1.
먼저 `ans` 배열이 비어있는 상태에서 (아직 정수가 하나도 들어오지 않은 상태) 체크하는 문자가
문자로 시작한다면 0을 *문자('.' 포)로 시작하면 0을 return 합니다.* 조건에 의해서 0을 return합니다.

또는 `ans` 배열에 값이 들어 있는데 문자를 만난다면 *숫자로 시작하다가 문자가 나타나면 숫자 부분만 반환합니다.* 조건에 의해 반복문을 `break`합니다.

마지막으로 문자가 정수나 operator라면 `ans`배열에 값을 추가해줍니다.

반복문을 탈출했다면 `ans` 배열에 값이 온전한 **숫자**인지를 검증하기 위해 `''.join(ans).lstrip('+').lstrip('-').isdigit()`로 True or False를 확인합니다.
`+`또는 `-`를 제거하는 이유는 문자열이 온전히 숫자로만 이루어져 있지 않다면 `.isdigit()` 함수가 `False`를 반환하기 때문입니다.

이때만약 온전한 숫자로 값이 이루어져 있지 않다면, (가령 `[-]` 형태) 0을 return합니다.
이제 우리는 온전한 형태의 수를 얻었습니다.

하지만 문제의 마지막 조건 *32-bit signed integer의 범위를 넘어가면 32-bit integer의 최대 혹은 최소값을 반환합니다.* 에 의해서
만약 값을 넘어간다면 32-bit integer의 최대/최소 값을 반환하는 `check_out_of_range` 함수를 구현하여 return해 줍니다.

```python
from string import ascii_lowercase


class Solution:
    def check_out_of_range(self, ans):
        if -2 ** 31 >= ans:
            return -2 ** 31
        elif 2 ** 31 <= ans:
            return 2 ** 31 - 1
        else:
            return ans

    def myAtoi(self, s: str) -> int:
        if len(s) < 1:
            return 0
        ans = []
        OPERATOR = ('+', '-')
        for char in s:
            if not ans and char in ascii_lowercase + '.':
                return 0
            if ans and char.isdigit() is False:
                break
            if char.isdigit() or char in OPERATOR:
                ans.append(char)
        # Check ans is digit
        ans = int(''.join(ans)) if ''.join(ans).lstrip('+').lstrip('-').isdigit() else 0
        return self.check_out_of_range(ans)
```
