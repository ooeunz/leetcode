# [Gas Station]()

> 2020-01-11

### solve 1.
가장 쉬운 풀이법으론 brute force로 문제를 풀 수 있습니다.
`gas[i] >= cost[i]`인 index를 찾아서, 배열을 rotate한 이후에 시계 방향으로 한바퀴를 돌면서 가능한 케이스인지 확인하는 문제입니다.
해당 알고리즘의 time complexity는 O(n^2)입니다.

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