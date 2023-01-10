# [Maximum Depth of Binary Tree](https://leetcode.com/explore/interview/card/top-interview-questions-easy/94/trees/555/)

> 2020-11-29

Binary Tree를 순회해서 가장 깊은 곳의 depth를 알아내는 문제입니다.
기존의 코딩테스트에선 birary tree 자체를 직접 구현한 알고리즘 문제를 풀어보지 않아서 tree 구조를 다루는 것에 익숙하지 않아서 조금 헷갈렸던 문제입니다.

### solve 1.
알고리즘 자체는 단순합니다. 
재귀 함수를 호출해서 마지막 node에 도착하면 해당 위치의 `depth`를 return해서 다시 위로 올라가면서 
다른 재귀 호출된 값과 `max`값을 비교하는 알고리즘 입니다.

```python
class Solution:
    def find_depth(self, node: TreeNode, depth: int):
        if node is None:
            return depth
        return max(self.find_depth(node.left, depth + 1), self.find_depth(node.right, depth + 1))

    def maxDepth(self, root: TreeNode) -> int:
        return self.find_depth(root, 0)
```