# [Factorial Trailing Zeroes](https://leetcode.com/problems/factorial-trailing-zeroes/submissions/)

> 2020-12-09

주어진 수 `n`의 factorial을 구했을 때, 팩토리얼 수의 마지막 0 이상의 수 이후로 0이 몇개 있는지를 return 하는 문제입니다.

### solve 1.
해당 풀이에선 간편하게 `math.factorial()`를 사용했지만 아래와 같이 recursive를 이용해 팩토리얼을 구할 수도 있습니다.
```python
def factorial_recursive(self, n):
    return n * self.factorial(n - 1) if n > 1 else 1
```

먼저 팩토리얼 값을 구한다음 문자열로 변환합니다. 그 후 뒤에서 부터 차례로 하나씩 값을 검사하며 만약 element가 `0`이라면 `ans`에 1을 더해주고,
만약 `0`이 아니라면 `ans`를 return 합니다.

```python
class Solution:
    def trailingZeroes(self, n: int) -> int:
        factorial = str(math.factorial(n))

        ans = 0
        for i in range(len(factorial) - 1, -1, -1):
            if factorial[i] == '0':
                ans += 1
            else:
                return ans
        return ans
```