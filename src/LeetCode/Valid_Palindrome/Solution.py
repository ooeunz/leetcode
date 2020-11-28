class Solution:
    def isPalindrome(self, s: str) -> bool:
        ss = ""
        for char in s.replace(" ", "").lower():
            if 48 <= ord(char) <= 57 or 97 <= ord(char) <= 122:
                ss += char
        return ss == "".join(list(reversed(ss)))


s = Solution()
print(s.isPalindrome("A man, a plan, a canal: Panama") == True)
print(s.isPalindrome("race a car") == False)

