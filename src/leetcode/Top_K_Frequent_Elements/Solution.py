from typing import List
import collections


class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        items = sorted(collections.Counter(nums).items(), key=lambda x: x[1], reverse=True)
        return [items[i][0] for i in range(k)]


s = Solution()
print(s.topKFrequent([1, 1, 1, 2, 2, 3], 2))
