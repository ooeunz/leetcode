# [Grumpy Bookstore Owner](https://leetcode.com/problems/grumpy-bookstore-owner/submissions/)

상점에 들리는 손님의 수를 나타내는 `customers` 배열이 주어집니다.
그리고 동일한 길이의 `grumpy` 배열이 주어집니다. `grumpy[i]`의 값이 1인 경우, 주인은 심술을 부리게 되고,
`customers[i]`에 방문한 손님들은 서비스에 불만족하고 돌아가게 됩니다.

이때 `X`번 만큼 주인이 심술 궃지 않게하는 기술이 있을 때, 최대한 많은 수의 손님이 서비스에 만족하고 돌아갈 수 있게 하는 알고리즘 입니다.

### solve 1.
이 문제는 **sliding window** 알고리즘을 이용해서 풀 수 있습니다.
먼저 `ans` 변수에 주인이 화가나지 않았을 때의 값을 날을 모두 더해줍니다.
그리고 동시에 화가나지 않았을 때의 값들은 모두 `0`으로 초기화 해줍니다. (중복 연산이 되지 않도록)

그런 다음 X만큼의 범위를 이동하면서 최대 값을 찾아줍니다.
이때 범위를 이동하는 방법으론 `X`만큼 더한 값(`cur`)을 옆으로 이동하면서
한칸 오른쪽으로 이동할때마다 `cur`에 오른쪽 index의 값을 더하고 가장 왼쪽의 값을 빼줍니다. (window를 움직임)

이와 같은 방법으로 window를 옮겨가며 `best_solution`에 `cur`값과 이전의 `best_solution`값을 비교해가며 가장 큰 합을 구하게됩니다.
for문을 탈출하게 되면 `ans`(심술 궃지 않았을때의 값)와 `best_solution`(X만큼 심술 궃지않게 했을 때 가장 큰 경우)를 더해서 return 하게 됩니다.

```python
class Solution:
    def maxSatisfied(self, customers: List[int], grumpy: List[int], X: int) -> int:
        ans = 0
        for i in range(len(grumpy)):
            if grumpy[i] == 0:
                ans += customers[i]
                customers[i] = 0
        best_solution = 0
        cur = 0
        for i, customer in enumerate(customers):
            cur += customer
            if i >= X:
                cur -= customers[i - X]
            best_solution = max(best_solution, cur)
        return ans + best_solution
```