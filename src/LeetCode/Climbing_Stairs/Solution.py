class Solution:
    d = {}
    def climbStairs(self, n: int) -> int:
        if n == 1 or n == 2 or n == 3:
            return n
        if n in self.d:
            return self.d[n]
        self.d[n] = self.climbStairs(n - 1) + self.climbStairs(n - 2)
        return self.d[n]


s = Solution()
print(s.climbStairs(2) == 2)
print(s.climbStairs(3) == 3)
print(s.climbStairs(38) == 63245986)
