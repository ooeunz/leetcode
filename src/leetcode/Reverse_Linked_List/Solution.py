class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


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
