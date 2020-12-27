from typing import List
from collections import Counter
import heapq


class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        counter = Counter(tasks)
        heap, ans = [], 0
        for v in counter.values():
            heapq.heappush(heap, -v)
        while heap:
            idle, cycle = 0, []
            while idle <= n:
                ans += 1
                if heap:
                    v = heapq.heappop(heap)
                    if v != -1:
                        cycle.append(v + 1)
                if not heap and not cycle:
                    return ans
                else:
                    idle += 1
            for v in cycle:
                heapq.heappush(heap, v)
        return ans


s = Solution()
print(s.leastInterval(["A", "A", "A", "B", "B", "B"], 2) == 8)
print(s.leastInterval(["A", "A", "A", "A", "A", "A", "B", "C", "D", "E", "F", "G"], 2) == 16)
