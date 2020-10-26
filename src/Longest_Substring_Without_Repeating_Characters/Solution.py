class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        start = end = 0
        package = set()
        while end < len(s):
            if start > end:
                return len(max(package, key=len))
            if s[start:end] not in package:
                package.add(s[start:end])
                end += 1
            else:
                start += 1
        return len(max(package, key=len))


s = Solution()
print(s.lengthOfLongestSubstring('abcabcbb'))
