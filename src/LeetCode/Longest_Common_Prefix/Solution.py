from typing import List


class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if not strs:
            return ""
        ans = ""
        strs.sort(key=lambda x: len(x), reverse=True)
        firstString = strs[0]
        for i in range(len(firstString) + 1):
            for idx, str in enumerate(strs):
                if not str.startswith(firstString[:i]):
                    break
                elif str.startswith(firstString[:i]) and idx == len(strs) - 1:
                    ans = firstString[:i]
        return ans


s = Solution()
print(s.longestCommonPrefix(["flower", "flow", "flight"]) == "fl")
print(s.longestCommonPrefix(["dog", "racecar", "car"]) == "")
