class Solution:
    def countSubstrings(self, s: str) -> int:
        ans = 0
        for i in range(len(s)):
            for j in range(i + 1, len(s) + 1):
                compare = s[i:j]
                if compare == compare[::-1]:
                    ans += 1
        return ans


s = Solution()
print(s.countSubstrings("abc"))
print(s.countSubstrings("aaa"))
