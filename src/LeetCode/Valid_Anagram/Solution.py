class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        return set(s) == set(t)


s = Solution()
print(s.isAnagram("anagram", "nagaram") == True)
print(s.isAnagram("rat", "car") == False)
