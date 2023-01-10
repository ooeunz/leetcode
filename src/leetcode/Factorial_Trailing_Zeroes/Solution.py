import math


class Solution:
    def trailingZeroes(self, n: int) -> int:
        factorial = str(math.factorial(n))

        ans = 0
        for i in range(len(factorial) - 1, -1, -1):
            if factorial[i] == '0':
                ans += 1
            else:
                return ans
        return ans


s = Solution()
print(s.trailingZeroes(5) == 1)
print(s.trailingZeroes(7) == 1)
