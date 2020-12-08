from typing import List


class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        ans = []
        compare = []
        for str in strs:
            sort = "".join(sorted(list(str)))
            if sort in compare:
                for i in range(len(compare)):
                    if compare[i] == sort:
                        ans[i].append(str)
            else:
                compare.append(sort)
                ans.append([str])
        return ans


s = Solution()
print(s.groupAnagrams(["eat", "tea", "tan", "ate", "nat", "bat"]))
