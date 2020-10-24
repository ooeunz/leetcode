# [Two Sum](https://leetcode.com/problems/add-two-numbers/)

> 2020-10-24

기존에 Java로 문제를 풀던 방식에서 다시 python으로 language를 변경했습니다. 아무래도 python이 기본적으로 구현되어있는 datastructure가 많기도하고, 언어 자체가 가장 수도 코드에 가깝기 때문에 가장 알고리즘 자체에 집중할 수 있는 언어라는 생각이 들었기 때문입니다.

### solve 1.
이 문제는 Linked List를 아느냐 모르느냐에 따라서 난이도가 많이 갈리는 문제입니다. 하나의 객체 안에 next로 다음 Node를 계속해서 뽑아내어 두 linked list의 값을 덧셈해야합니다.

문제 풀이의 편의를 위해 먼저 두개의 list를 선언했고, 그 안에 ListNode의 모든 val을 뽑아내어 담았습니다. 
그 이후 두 list의 길이가 다를 수 있기 때문에 while문으로 두 list를 순회하였고, 값을 더하여 10 이상일 경우 다음 index의 값에 더해주었습니다.

마지막으로 문제의 return 형식에 맞춰서 ListNode에 다시 값을 추가해주는 방식을 사용했는데, while문 자체를 돌면서 ListNode를 바로 구현할 수는 없을까? 라는 의문이 드는 문제입니다. 
```python
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

```