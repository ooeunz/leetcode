from typing import List


class Solution(object):
    def generateParenthesis(self, n: int) -> List[str]:
        ans = []
        OPEN, CLOSE = '(', ')'

        def backtracking(s: str, open: int, close: int):
            if len(s) == n * 2:
                ans.append(s)
            if open < n:
                backtracking(s + OPEN, open + 1, close)
            if close < open:
                backtracking(s + CLOSE, open, close + 1)
        backtracking('', 0, 0)
        return ans


s = Solution()
print(s.generateParenthesis(3))
print(s.generateParenthesis(1))
