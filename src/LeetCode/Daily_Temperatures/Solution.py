from typing import List


class Solution:
    def dailyTemperatures(self, T: List[int]) -> List[int]:
        stack = []
        ans = [0] * len(T)
        for i in range(len(T)):
            if not stack or T[stack[-1]] > T[i]:
                stack.append(i)
            else:
                while stack and T[stack[-1]] < T[i]:
                    j = stack.pop()
                    ans[j] = i - j
                stack.append(i)
        return ans


s = Solution()
print(s.dailyTemperatures([73, 74, 75, 71, 69, 72, 76, 73]))
