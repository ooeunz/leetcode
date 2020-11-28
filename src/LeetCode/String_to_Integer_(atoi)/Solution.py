class Solution:
    def check_out_of_range(self, ans):
        if -2 ** 31 >= ans:
            return -2 ** 31
        elif 2 ** 31 <= ans:
            return 2 ** 31 - 1
        else:
            return ans

    def myAtoi(self, s: str) -> int:
        if len(s) < 1:
            return 0

        ans = []
        OPERATOR = ('+', '-')
        # If s[0] is letter
        if s[0].isspace() or s[0].isdigit() is True or s[0] in OPERATOR:
            for char in s:
                if not ans \
                        and char.isdigit() is False \
                        and char not in OPERATOR\
                        and char.isspace() is False:
                    return 0
                if ans and char.isdigit() is False:
                    break
                if char.isdigit() or char in OPERATOR:
                    ans.append(char)
            # Check ans is digit
            ans = int(''.join(ans)) if ''.join(ans).lstrip('+').lstrip('-').isdigit() else 0
            return self.check_out_of_range(ans)
        else:
            return 0


s = Solution()
print(s.myAtoi('42') == 42)
print(s.myAtoi('   -42') == -42)
print(s.myAtoi('+1') == 1)
print(s.myAtoi('4193 with words') == 4193)
print(s.myAtoi('words and 987') == 0)
print(s.myAtoi('-91283472332') == -2147483648)
print(s.myAtoi('3.14159') == 3)
print(s.myAtoi('-+12') == 0)
print(s.myAtoi('.1') == 0)
print(s.myAtoi('') == 0)
print(s.myAtoi(' ') == 0)
