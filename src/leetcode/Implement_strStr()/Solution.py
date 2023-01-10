class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        if haystack == needle:
            return 0
        for i in range(len(haystack)):
            if haystack[i:].startswith(needle):
                return i
        return -1


s = Solution()
print(s.strStr('hello', 'll') == 2)
print(s.strStr('aaaaa', 'bba') == -1)
print(s.strStr('', '') == 0)
