from typing import List


class Solution:
    def reverseString(self, s: List[str]) -> None:
        start, end = 0, len(s) - 1
        while start < end:
            s[start], s[end] = s[end], s[start]
            start, end = start + 1, end - 1

        # This is nothing to do with the answer
        print(s)


s = Solution()
s.reverseString(["h", "e", "l", "l", "o"])  # ["o", "l", "l", "e", "h"]
s.reverseString(["H", "a", "n", "n", "a", "h"])  # ["h", "a", "n", "n", "a", "H"]
