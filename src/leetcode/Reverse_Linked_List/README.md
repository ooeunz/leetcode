# [Reverse Linked List](https://leetcode.com/explore/interview/card/top-interview-questions-easy/93/linked-list/560/)

> 2020-11-29

주어진 Linked List를 뒤집는 문제입니다.

### solve 1.
첫번째 풀이 방법은 Linked List에 포함된 val를 모두 꺼내서 `val_lst`에 넣어준 다음, 배열을 뒤집어 새로운 Linked List를 만드는 것입니다.

현재 마지막 노드의 위치를 저장하는 pointer `ptr` 변수를 이용해 `val_lst`를 순회하며 새로운 node를 하나씩 추가합니다.
```python
class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        val_lst = []
        ans = None
        while head is not None:
            val_lst.append(head.val)
            head = head.next

        ptr = None
        if val_lst:
            reverse_lst = list(reversed(val_lst))
            for i in range(len(reverse_lst)):
                if i == 0:
                    ans = ptr = ListNode(reverse_lst[i])
                else:
                    ptr.next = ListNode(reverse_lst[i])
                    ptr = ptr.next
            ptr.next = None
        return ans
```