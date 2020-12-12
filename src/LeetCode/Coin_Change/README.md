# [Coin Change](https://leetcode.com/explore/interview/card/top-interview-questions-medium/111/dynamic-programming/809/)

> 2020-12-12

배열에 동전의 종류가 주어졌을 때, 가장 적은 수의 동전으로 `target` 값을 구하는 문제입니다.
만약 구할 수 없다면 `-1`을 return 합니다.


### solve 1.
해당 문제는 dynamic programing으로 풀 수 있습니다. 모든 범위를 탐색할 수도 있지만 
그렇게 되면 너무 많은 경우의 수를 탐색해야 하기 때문에 time error가 날 확률이 높습니다.

먼저 `amount`가 `0`일때의 예외사항을 제외하고 문제를 풀어나갑니다.
`dp`라는 이름의 dictionary를 선언하는데, 특이하게 해당 dictionary의 default value는 정수 최대 값 `float('inf')`를 선언합니다.
정수 최댓값을 default value로 사용하는 이유는 dp안의 value는 최솟값을 저장해야하기 때문에 
비교의 대상으로 첫 비교시에는 어떤 정수가 오더라도 `float('inf')`와 비교하여 value로 저장될 수 있도록 하기 위해서입니다.

그런 다음 이제 for문을 이용해서 `1`부터 `amount`의 길이만큼 dp에 값을 채워나가게 됩니다.
`dp`의 각 key값은 현재까지의 값에 대하여 필요한 최소한의 동전의 수입니다.

문제에 주어지는 동전은 여러 개 이기 때문에, for 문을 이용해서 사용하려는 동전을 이용해서 해당 key값에 도달할 수 있는지를 확인합니다.
(그리고 동전 하나만을 사용하여 해당 key값에 도달할 수 있으므로 동전의 크기와 key값이 같은 경우엔 하나의 동전만을 사용했다는 의미로 1을 value로 넣어줍니다.)

하나의 key 값에 다양한 동전을 이용해 비교해가며 최솟값을 부여해가며 목표로했던 `amount`까지 값을 채우게 됩니다.
for문이 끝나고 `dp[amount]`값이 `float('inf')`가 아니라면, 즉 주어진 동전으로 만들 수 있는 수라면 `dp[amount]`값을 return하고,
그렇지 않다면 `-1`을 return합니다.

```python
class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        if amount == 0:
            return 0
        dp = collections.defaultdict(lambda: float('inf'))
        for i in range(1, amount + 1):
            for coin in coins:
                if coin <= amount and dp[coin] == float('inf'):
                    dp[coin] = 1

                prev_coin = i - coin
                if 0 < prev_coin < float('inf'):
                    dp[i] = min(dp[prev_coin] + 1, dp[i])
        return dp[amount] if dp[amount] < float('inf') else -1
```

### solve 2.
처음 저만의 풀이법으로 해당 문제를 풀었지만,
이 후 풀이를 보고 다시 실행시키니 run time이 많이 차이가 나서 Leetcode 풀이 방식도 추가합니다..

풀이에 사용한 알고리즘은 top down 방식의 dynamic programing 이고, recursion을 이용해 구현하였습니다.
`dp` dictionary에는 `key: value = amount - 1 : 최소로 필요한 동전의 수`가 저장됩니다.
> 사실 이 부분에서 조금 이해가 가지 않는 부분이 `amount - 1`이 아니라 `amount`로 하게되면 time error가 발생하게 되는데, 어떤 차이가 있는지 잘 이해가 가지 않습니다. 😭

사용할 수 있는 coin이 여러 개 이기 때문에 coins를 for문을 돌며 하나씩 해당 현재 `amount`에서 해당 coin을 사용할 수 있는지를 검사합니다.
그리고 만약 유효한 값이라면 `dp`에 저장하고 해당 값을 return합니다.

아래는 위 설명을 구현한 코드입니다.

```python
class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        if amount < 0:
            return 0
        dp = collections.defaultdict(lambda: float('inf'))
        return self.coin_change(coins, amount, dp)

    def coin_change(self, coins: list, amount: int, dp):
        if amount < 0:
            return -1
        if amount == 0:
            return 0
        if amount - 1 in dp:
            return dp[amount - 1]
        mn = float('inf')
        for coin in coins:
            res = self.coin_change(coins, amount - coin, dp)
            if 0 <= res < mn:
                mn = res + 1
        dp[amount - 1] = mn if mn != float('inf') else -1
        return dp[amount - 1]
``` 