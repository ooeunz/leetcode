# [Generate Parentheses](https://leetcode.com/problems/generate-parentheses/submissions/)

> 2020-12-13

온전하게 열고 닫힌 괄호의 수 `n`이 주어 졌을 때, 주어진 괄호를 이용해서 나올 수 있는 모든 조합을 return하는 문제입니다.

### solve 1.
해당 문제는 backtracking을 이용해서 풀 수 있습니다. 사실 backtracking이란 recursion과 크게 차이가 없는데,
기존의 recursion function에서 termination check가 부가적으로 들어간 알고리즘 기법이라고 생각하시면 됩니다.
즉, 특정 조건이 성립 했을 때 (현재 문제로 치면 open된 괄호와 close된 괄호의 수가 맞지 않을 때) 더이상 recursion을 수행하지 않고 termination하는 것을 뜻합니다.

아래의 코드를 보시겠습니다. backtracking이라는 함수를 선언하고 내용을 살펴봅니다.
가장 먼저 현재까지 늘어난 문자열의 길이가 `n * 2`일때 정답을 추가하도록 합니다. (여기서 `n * 2`인 이유는 괄호의 쌍을 합하면 `* 2`가 되기 때문입니다.)

그리고 resursion을 수행하는 조건을 추가해주는데, `open`의 수가 `n`보다 작으면 `s`에 `(`를 추가해줍니다.
그리고 `open`의 수만큼 `close`의 수 역시 동일하게 존재해야 하기 때문에 `close < open`이라면 `close`를 추가하여 recursion을 수행해줍니다.

backtracking이 끝나면 `ans` 배열을 return합니다. 
 
```python
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
```