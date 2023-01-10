from typing import List
import collections


class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        ans = collections.defaultdict(list)
        for str in strs:
            ans[tuple(sorted(str))].append(str)
        return list(ans.values())


s = Solution()
print(s.groupAnagrams(["eat", "tea", "tan", "ate", "nat", "bat"]))
