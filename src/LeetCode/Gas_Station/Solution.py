from typing import List


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


s = Solution()
print(s.canCompleteCircuit([1, 2, 3, 4, 5], [3, 4, 5, 1, 2]))
print(s.canCompleteCircuit([2, 3, 4], [3, 4, 3]))
