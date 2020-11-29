class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


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
