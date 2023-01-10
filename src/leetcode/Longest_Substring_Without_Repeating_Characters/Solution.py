class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) < 2:
            return len(s)
        start = 0
        end = 1
        pkg = set(list(s[start:end]))
        mx = len(pkg)
        while end < len(s):
            while s[end] in pkg:
                pkg.remove(s[start])
                start += 1
            if start >= end:
                pkg.add(s[start])
                end += 1
            elif s[end] not in pkg:
                pkg.add(s[end])
                mx = max(mx, len(pkg))
                end += 1
        return mx


s = Solution()
print(s.lengthOfLongestSubstring("abcabcbb") == 3)
print(s.lengthOfLongestSubstring("bbbbb") == 1)
print(s.lengthOfLongestSubstring("pwwkew") == 3)
print(s.lengthOfLongestSubstring("") == 0)
print(s.lengthOfLongestSubstring("aab") == 2)

