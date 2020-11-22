class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def valueExtractor(self, lst: ListNode):
        result = []
        while lst is not None:
            result.append(lst.val)
            lst = lst.next
        return result

    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        l1_lst = self.valueExtractor(l1)
        l2_lst = self.valueExtractor(l2)

        over_num = 0
        ans = []

        i = 0
        max_len = max(len(l1_lst), len(l2_lst))
        while i < max_len:
            fir, sec = 0, 0
            if len(l1_lst) > i:
                fir = l1_lst[i]
            if len(l2_lst) > i:
                sec = l2_lst[i]
            div, mod = divmod(fir + sec + over_num, 10)
            ans.append(str(mod))
            over_num = 0 or div
            i += 1
        if over_num:
            ans.append(over_num)

        listNode = ListNode(ans[-1])
        for i in range(len(ans)-2, -1, -1):
            listNode = ListNode(ans[i], listNode)
        return listNode
