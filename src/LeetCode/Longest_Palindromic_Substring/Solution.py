class Solution:
    def longestPalindrome(self, s: str) -> str:
        mx = 0
        ans = []
        dic = {val: [] for val in set(s)}
        for i, val in enumerate(s):
            dic[val].append(i)
            for j in range(len(dic[val])):
                start = dic[val][j]
                end = dic[val][-1] + 1
                if end - start > mx and s[start:end] == ''.join(reversed(s[start:end])):
                    mx = end - start
                    ans = [start, end]
        return s[ans[0]:ans[1]]


s = Solution()
print(s.longestPalindrome("babad") == "bab" or s.longestPalindrome("babad") == "aba")
print(s.longestPalindrome("cbbd") == "bb")
print(s.longestPalindrome("a") == "a")
print(s.longestPalindrome("ac") == "a")
