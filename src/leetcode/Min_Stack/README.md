# [Min Stack](https://leetcode.com/problems/min-stack/submissions/)

> 2020-12-14

Stack을 직접 구현하는 문제입니다.

### solve 1.
문제엔 push, pop, top, getMin을 구현했지만, 그 외에도 `isEmpty`, `isFull`, `clear`, `printStack` 등을 구현할 수 있습니다.

```python
class MinStack:

    def __init__(self):
        self.stack = []

    def push(self, x: int) -> None:
        self.stack.append(x)

    def pop(self) -> None:
        self.stack.pop()

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return min(self.stack)
```