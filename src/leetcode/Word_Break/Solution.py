from typing import List


class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        dp = [1] + [0] * (len(s) - 1)
        for i in range(len(s)):
            if dp[i]:
                for word in wordDict:
                    if s[i:].startswith(word):
                        if i + len(word) == len(s):
                            return True
                        elif i + len(word) < len(s):
                            dp[i + len(word)] = 1
        return False


s = Solution()
print(s.wordBreak("leetcode", ["leet", "code"]) is True)
print(s.wordBreak("catsandog", ["cats", "dog", "sand", "and", "cat"]) is False)
print(s.wordBreak(
    "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaab",
    ["a", "aa", "aaa", "aaaa", "aaaaa", "aaaaaa", "aaaaaaa", "aaaaaaaa", "aaaaaaaaa", "aaaaaaaaaa"]) is False)
