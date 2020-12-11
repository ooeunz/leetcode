# [Jump Game](https://leetcode.com/explore/interview/card/top-interview-questions-medium/111/dynamic-programming/807/)

> 2020-12-11

음수가 아닌 정수로 이루어진 배열이 있을 때, 해당 배열의 값 이하만큼 index를 점프할 수 있습니다.
이때 마지막 index에 도착할 수 있는지를 구하는 문제입니다.

### solve 1.
모든 경우의 수를 계산하게 될 경우 너무 많은 경우의 수가 존재하기 때문에 해당 문제는 dynamic programing을 이용해서 풀 수 있습니다.
먼저 최적해를 저장하는 dp 배열을 선언합니다.

해당 배열은 각 element들은 해당 index에서 갈 수 있는 최대 값들이 누적되어 온 값입니다.

이제 배열의 두번째 index부터 배열을 순회하기 시작합니다. (문제에서 nums는 1이상이라는 조건을 주었기 때문에 1부터 시작합니다.)
만약 `dp`배열에 `i - 1`값이 0보다 크다면, 해당 현재 `dp[i]`에 `dp[i - 1]`(이전까지의 최적해)와 현재의 값을 비교하여 큰 값을 저장해줍니다.

그런데 만약 for문을 도는 중에 `dp[i - 1]`값이 `0`이라면 앞에서 어떤 경우의 수를 계산하더라도 `i`번째 index에 도달할 수 없으므로 `False`를 반환합니다.
반대로 for문을 무사히 끝냈다면 마지막 index에 도착할 수 있다는 뜻이므로 `True`값을 반환합니다.

해당 알고리즘은 `nums`배열의 길이만큼 for문을 돌기 때문에 time complexity는 `O(n)`입니다. 
 
```python
class Solution:
    def canJump(self, nums: List[int]) -> bool:
        dp = [nums[0]] + [0] * (len(nums) - 1)
        for i in range(1, len(nums)):
            if dp[i - 1]:
                dp[i] = max(dp[i - 1] - 1, nums[i])
            else:
                return False
        return True
```