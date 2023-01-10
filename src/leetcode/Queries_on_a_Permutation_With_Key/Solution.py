from typing import List


class Solution:
    def processQueries(self, queries: List[int], m: int) -> List[int]:
        p = [i for i in range(1, m + 1)]
        ans = []
        for query in queries:
            pos = p.index(query)
            ans.append(pos)
            p = [p[pos]] + p[:pos] + p[pos + 1:]
        return ans


s = Solution()
print(s.processQueries([3, 1, 2, 1], 5) == [2, 1, 2, 1])
print(s.processQueries([4, 1, 2, 2, ], 4) == [3, 1, 2, 0])
