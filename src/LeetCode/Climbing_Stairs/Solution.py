class Solution:
    def climbStairs(self, n: int) -> int:
        if n < 0:
            return 0
        elif n == 0:
            return 1
        else:
            return self.climbStairs(n - 1) + self.climbStairs(n - 2)


s = Solution()
print(s.climbStairs(2) == 2)
print(s.climbStairs(3) == 3)
print(s.climbStairs(38) == 63245986)
