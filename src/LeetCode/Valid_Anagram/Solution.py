from collections import Counter


class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        return Counter(s) == Counter(t)


s = Solution()
print(s.isAnagram("anagram", "nagaram") == True)
print(s.isAnagram("rat", "car") == False)
