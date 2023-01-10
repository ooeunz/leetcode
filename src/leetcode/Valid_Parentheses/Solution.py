class Solution:
    def isValid(self, s: str) -> bool:
        BRACKET = {
            '(': ')',
            '[': ']',
            '{': '}',
        }
        stack = []
        for ss in s:
            if ss in BRACKET.keys():
                stack.append(ss)
            elif ss in BRACKET.values():
                if len(stack) == 0 or BRACKET[stack.pop()] != ss:
                    return False
        return False if stack else True


s = Solution()
print(s.isValid("()") is True)
print(s.isValid("()[]{}") is True)
print(s.isValid("(]") is False)
print(s.isValid("([)]") is False)
print(s.isValid("{[]}") is True)
