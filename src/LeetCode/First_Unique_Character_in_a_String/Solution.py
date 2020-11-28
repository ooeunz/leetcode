from collections import Counter

class Solution:
    def firstUniqChar(self, s: str) -> int:
        cnt = Counter(list(s))
        for idx, val in enumerate(s):
            if cnt[val] == 1:
                return idx
        return -1


s = Solution()
print(s.firstUniqChar("leetcode") == 0)
print(s.firstUniqChar("loveleetcode") == 2)
