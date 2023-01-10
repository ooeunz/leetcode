# [Remove Nth Node From End of List](https://leetcode.com/explore/interview/card/top-interview-questions-easy/93/linked-list/603/)

> 2020-11-29

Linked List가 주어졌을 때 뒤에서부터 `n`만큼 앞에 있는 node를 지우는 문제입니다.

### solve 1.
> Follow up: Could you do this in one pass?

해당 풀이법은 하나의 Follow up 기준을 충족한 알고리즘으로 하나의 path로 알고리즘을 풀이합니다.

알고리즘의 핵심적인 풀이 방법은 `Two pointer` 알고리즘을 사용하는 것입니다. 두개의 포인터를 Linked List에 흘리는데 각각의 pointer는 n만큼의 간격을 두고 이동합니다.
때문에 먼저 출발한 first pointer가 Node의 끝에 도착하면 second pointer가 `next`로 가리키고 있는 node가 끝에서 `n`번째인 node가 되는 알고리즘입니다.

제일 먼저 `head`를 `next`로 갖는 3개의 pointer를 생성합니다. 그럼 `[dummy] -> [node1] -> [node] ...`의 형태로 header 앞에 pointer가 위치하게 되는데,
이때 `header`에서 시작하지 않는 이유는 Linked List에서 node를 지우는 방법과 관련이 있는데, 
`n`번째에 있는 node를 삭제하기 위해서는 pointer가 `n`번째 이전의 node에서 `n + 1`번째의 node를 가리키는 방법으로 node를 삭제하기 하기 때문입니다.

따라서 node가 한개 뿐인 Linked List를 삭제하기 위해선 `head` 이전에 pointer가 위치할 필요가 있습니다.

다시 알고리즘으로 돌아와서 dummy에서 부터 `first` pointer를 `n + 1`만큼(first pointer와 second pointer 사이에 n만큼의 공간을 남기기 위해) 이동시켜 줍니다.
그 후, `first` pointer가 None이 될 때까지 `first`pointer와 `second`pointer를 함께 이동시켜줍니다.
이때 `first` pointer가 Node이 된다면 `second` pointer는 Linked List의 뒤에서 `n`번째 위치한 node의 앞 node에 위치하게 됩니다.

이제 `second` pointer를 이용해 `n`번째 node를 지워준 다음, `dummy` pointer의 `next`에 있는 `head`를 return시켜줍니다.
```python
class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        first = second = dummy = ListNode(0)
        dummy.next = head
        for _ in range(n + 1):
            first = first.next
        while first is not None:
            first = first.next
            second = second.next
        second.next = second.next.next
        return dummy.next
```