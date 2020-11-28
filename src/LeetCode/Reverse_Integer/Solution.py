class Solution:
    def reverse(self, x: int) -> int:
        if x < 0:
            ans = -int(''.join(list(reversed(str(abs(x))))))
            return 0 if ans < -2 ** 31 else ans
        else:
            ans = int(''.join(list(reversed(str(x)))))
            return 0 if ans > 2 ** 31 else ans


s = Solution()
print(s.reverse(123) == 321)
print(s.reverse(-123) == -321)
print(s.reverse(-123) == -321)
print(s.reverse(120) == 21)
print(s.reverse(0) == 0)
print(s.reverse(1534236469) == 0)
