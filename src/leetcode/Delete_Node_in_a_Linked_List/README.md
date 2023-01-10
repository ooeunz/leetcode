# [Delete Node in a Linked List](https://leetcode.com/explore/interview/card/top-interview-questions-easy/93/linked-list/553/)

> 2020-12-29데

Linked List 중간에 있는 Node 하나를 삭제하는 문제입니다.

### solve 1.
`node`가 LinkedList 라는 가정하에 문제를 풀게되는 되는데, 간단하게 다음 노드의 값을 호출하여 대입함으로써 문제를 풀 수 있습니다.

```python
class Solution:
    def deleteNode(self, node):
        node.val = node.next.val
        node.next = node.next.next
```