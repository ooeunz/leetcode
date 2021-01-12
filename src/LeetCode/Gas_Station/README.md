# [Gas Station](https://leetcode.com/problems/gas-station/submissions/)

> 2020-01-11

### solve 1.
가장 쉬운 풀이법으론 brute force로 문제를 풀 수 있습니다.
`gas[i] >= cost[i]`인 index를 찾아서, 배열을 rotate한 이후에 시계 방향으로 한바퀴를 돌면서 가능한 케이스인지 확인하는 문제입니다.
해당 알고리즘의 time complexity는 `O(n^2)`입니다.

```python
class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        if sum(cost) > sum(gas):
            return -1
        for i in range(len(gas)):
            if gas[i] >= cost[i]:
                gas_start = gas[i:] + gas[:i]
                cost_start = cost[i:] + cost[:i]

                def is_possible(gas_start, cost_start):
                    tank = 0
                    for g, c in zip(gas_start, cost_start):
                        tank += g
                        tank -= c
                        if tank < 0:
                            return False
                    return True
                if is_possible(gas_start, cost_start):
                    return i
        return -1
```

### solve 2.
두번 째 방법은 `O(n)` 만큼의 time complexity를 사용해서 풀이하는 방법입니다.
먼저 `0`을 값으로 갖는 3가지 변수를 선언해줍니다.
- `start`: 출발하는 index를 가리킵니다.
- `acc`: `start`를 검증하는 값으로, `start`부터 시작해서 현재까지의 합을 저장합니다.
- `total`: 전체 `gas - cost`의 값을 저장합니다.

`i = 1`일때 `acc >= 0`이라면 `i = 0`일때도 `acc >= 0`입니다.
이러한 특징을 이용해서 `acc`가 `0`보다 작아질 때, `start`를 현재 `i`보다 1크게 갱신해줍니다. (어디서 부터 start해야할지 찾는 작업)
for문을 모두 끝내게 되었을 때 `total`의 값이 `0`보다 큰지 확인해줍니다.

만약 `total`이 0보다 작다는 것은 모든 `gas`의 합에서 `cost`를 빼게 되었을 때 그 값이 부족하다는 뜻이 됩니다.
이는 어떤 경우에 출발하더라도 한바퀴를 돌 수 없다는 것을 의미하므로 `-1`을 return 합니다.

To solve this problem, I declare three variable. like start, acc, total.

- start means index position,
- acc is sum of from start to current index,
- And total is mean sum of entire gas - cost.

if value of acc greater than zero, it is prove that indexes less than i are better than zero.
  
When i execute for loop as much length of gas.
if value of acc is smaller than zero, we have to reinitialize acc, and move start point to i + 1.

Finally, when we escape for loop, we have to check about value of total.
if total greater than 0, it's mean possible that you can travel around the circuit.
but if total smaller than zero it's mean impossible. so this function will be return -1.
  
```python
class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        start = acc = total = 0
        for i in range(len(gas)):
            acc += (gas[i] - cost[i])
            total += (gas[i] - cost[i])
            if acc < 0:
                acc = 0
                start = i + 1
        return start if total >= 0 else -1
```