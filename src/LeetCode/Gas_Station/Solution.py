from typing import List


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


s = Solution()
print(s.canCompleteCircuit([1, 2, 3, 4, 5], [3, 4, 5, 1, 2]) == 3)
print(s.canCompleteCircuit([2, 3, 4], [3, 4, 3]) == -1)
