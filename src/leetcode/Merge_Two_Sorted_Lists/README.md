# [Merge Two Sorted Lists](https://leetcode.com/explore/interview/card/top-interview-questions-easy/93/linked-list/771/)

> 2020-11-29

두개의 Linked List가 주어졌을 때 두개의 list를 정렬하여 merge하는 문제입니다.

### solve 1.
`val_lst`에 두 Linked List의 값들을 정렬해가며 채운 후 순서대로 배열을 순회하며 하나씩 `ans` Linked List에 node로 추가해주는 풀이입니다.

이때 `l1`, `l2` Linked List 두개 다 값이 비어있을 수 있으므로 예외처리를 해줍니다.
두 Linked List를 while문을 이용해 값을 담고, 만약 하나의 Linked List에 값이 아직 남아 있을 경우를 위해 
`mod = l2 if l1 is None else l1`처럼 아직 node가 남아 있는 Linked List를 선택해 마저 `val_lst`에 담아줍니다.  
 
마지막으로 `val_lst` 배열을 순환하며 하나씩 `ans`Linked List의 node로 추가해줍니다.

```python
class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        ans = ptr = None
        if not l1 and not l2:
            return ans

        val_lst = []
        while l1 is not None and l2 is not None:
            if l1.val <= l2.val:
                val_lst.append(l1.val)
                l1 = l1.next
            else:
                val_lst.append(l2.val)
                l2 = l2.next

        mod = l2 if l1 is None else l1
        while mod is not None:
            val_lst.append(mod.val)
            mod = mod.next
        for idx, val in enumerate(val_lst):
            if idx == 0:
                ans = ptr = ListNode(val)
            else:
                ptr.next = ListNode(val)
                ptr = ptr.next
        ptr.next = None
        return ans
```