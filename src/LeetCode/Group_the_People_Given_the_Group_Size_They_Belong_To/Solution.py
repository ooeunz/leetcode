from typing import List
import collections


class Solution:
    def groupThePeople(self, groupSizes: List[int]) -> List[List[int]]:
        ans = []
        pkg = collections.defaultdict(list)
        for i in range(len(groupSizes)):
            pkg[groupSizes[i]].append(i)
            if len(pkg[groupSizes[i]]) == groupSizes[i]:
                ans.append(pkg[groupSizes[i]][:])
                pkg[groupSizes[i]] = []
        return ans


s = Solution()
print(s.groupThePeople([3,3,3,3,3,1,3]))
print(s.groupThePeople([2,1,3,3,3,2]))