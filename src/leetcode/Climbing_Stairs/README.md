# [Climbing Stairs](https://leetcode.com/explore/interview/card/top-interview-questions-easy/97/dynamic-programming/569/)

> 2020-12-03

주어진 수 `n`이 있을 때 1 또는 2만을 더해서 `n`이 될 수 있는 경우의 수가 몇개인지 구하는 문제입니다.

### solve 1.
가장 쉬운 방법은 dfs를 이용해서 완전 탐색을 하는 방법입니다. 
`n`에서 1 또는 2를 계속해서 빼서 값이 0이되면 하나의 방법을 찾았다는 의미로 `1`을 return해줍니다.
하지만 이 알고리즘은 `n`번만큼 2개의 재귀함수(`self.climbStairs(n - 1) + self.climbStairs(n - 2)`)를 호출하기 때문에 
time complexity가 `O(2^n)`으로 time error가 발생합니다.

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

### solve 2.
두번째 방법은 dynamic programing을 사용하는 방법입니다. dynamic programing, 이하 dp는 memoization을 이용하는 방식입니다.
여러개의 중복되는 연산의 값을 메모리에 저장해두고 동일한 연산을 필요로 하는 경우 새롭게 계산하는 것이 아니라 메모리에 저장된 값을 불러오는 방법입니다.

아래의 개선된 코드를 살펴보도록 하겠습니다. 먼저 기저 사례부분을 살펴보겠습니다.
만약 `n`이 `1`이라면 `[1]`이라는 하나의 step만을 사용할 수 있으므로 `1`을 return 해야합니다.
만약 `n`이 `2`라면, `[1, 1]`과 `[2]`라는 두개의 방법을 사용할 수 있으므로 `2`을 return 해야합니다.
만약 `n`이 `3`이라면 `[1, 1, 1]`, `[1, 2]`, `[2, 1]`와 같이 세가지 방법을 사용할 수 있으므로 `3`을 return 해야합니다.

따라서 해당하는 수가 될 때마다 `n`을 return 하도록 해줍니다.
그리고 그 다음 기저 사례로 만약 `n`이 이미 계산했던 값인지 확인하고 만약 값이 있다면 그 아래의 값들을 계산하지 않고 저장한 값을 불러와 return합니다.
만약 계산한 적이 없는 값이라면 값을 계산해서 `d`딕셔너리에 값을 저장 해준 후 값을 return 합니다.

이와 같은 알고리즘은 선형 시간만큼의 time complexity를 가지게 되므로 `O(n)`과 `n`만큼의 데이터를 저장할 메모리가 필요하기 때문에 space complexity 역시 `O(n)`입니다.

```python
class Solution:
    d = {}
    def climbStairs(self, n: int) -> int:
        if n == 1 or n == 2 or n == 3:
            return n
        if n in self.d:
            return self.d[n]
        self.d[n] = self.climbStairs(n - 1) + self.climbStairs(n - 2)
        return self.d[n]
```