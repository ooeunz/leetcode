# [Valid Parentheses](https://leetcode.com/problems/valid-parentheses/submissions/)

> 2020-12-12

괄호로 이루어진 문자열이 주어졌을 때, 괄호의 구성이 올바르게 열고 닫혔는지 확인하는 문제입니다.

### solve 1.
열리는 괄호라면 `stack`에 값을 추가해줍니다. 그리고 닫히는 괄호라면
`stack`에 1개 이상의 괄호가 존재하고, `stack`의 마지막 index에 존재하는 괄호와 쌍이 맞는지 확인합니다.

만약 이에 해당하지 않는 다면 `False`를 return합니다.

마지막으로 `stack`에 아직 남아있는 element가 있는지를 확인하고, 만약 남아있다면 괄호의 쌍이 맞지 않다는 뜻이므로 `False`를 return하고,
만약 쌍이 맞다면 `True`를 return합니다.

```python
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
```