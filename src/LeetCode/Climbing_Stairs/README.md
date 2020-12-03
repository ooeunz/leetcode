# [Climbing Stairs](https://leetcode.com/explore/interview/card/top-interview-questions-easy/97/dynamic-programming/569/)

> 2020-12-03

주어진 수 `n`이 있을 때 1 또는 2만을 더해서 `n`이 될 수 있는 경우의 수가 몇개인지 구하는 문제입니다.

### solve 1.
가장 쉬운 방법은 dfs를 이용해서 완전 탐색을 하는 방법입니다. `n`에서 1 또는 2를 계속해서 빼서 값이 0이되면 하나의 방법을 찾았다는 의미로 `1`을 return해줍니다.
하지만 이 알고리즘은 time error가 발생합니다.

```python
class Solution:
    def climbStairs(self, n: int) -> int:
        if n < 0:
            return 0
        elif n == 0:
            return 1
        else:
            return self.climbStairs(n - 1) + self.climbStairs(n - 2)

``` 