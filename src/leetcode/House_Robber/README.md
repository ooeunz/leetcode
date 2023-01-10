# [House Robber](https://leetcode.com/explore/interview/card/top-interview-questions-easy/97/dynamic-programming/576/)

> 2020-12-06

정수로만 이루어진 배열이 주어 졌을 때 바로 옆의 각 index들의 바로 옆 index를 제외한 나머지 index들을 더해서 최대 값을 return 하는 문제입니다.

### solve 1.
문제의 풀이법은 dynamic programing을 이용한 방법입니다.
먼저 주어진 `nums` 배열의 길이가 0이거나 1이거나 2일 경우 예외처리를 해줍니다.

그리고 그 이상의 길이일 경우에 `dp`라는 배열을 만들어줍니다.(이때 0과 1 index는 초기값을 지정해줍니다)
 `dp` 배열의 각각의 element들은 앞의 element들의 값들이 누적되어, 현재까지 구할 수 있는 최대 값을 저장하는 배열입니다.
 
이제 배열을 순환하게 되는데, 핵심은 
- 2개 이전의 가장 큰 값과 현재 값을 더했을 때의 값 (한칸 을 공백을 두고 점프했을 경우)
- 1개 이전의 가장 큰 값 (두 칸의 공백을 두더라도 이전의 값이 큰지 확인)
두가지를 비교하여 `dp[i]`에 최대 값을 저장해줍니다.

이와 같은 방식으로 dp의 전체 길이만큼 알고리즘을 수행하게 되므로 
알고리즘의 time complexity는 `O(n)`이고, space complexity는 `O(1)`입니다.

```python
class Solution:
    def rob(self, nums: List[int]) -> int:
        length = len(nums)
        if length == 0:
            return 0
        if length == 1:
            return nums[0]
        if length == 2:
            return max(nums)

        dp = [0] * length
        dp[0] = nums[0]
        dp[1] = max(nums[0], nums[1])

        for i in range(2, length):
            dp[i] = max(dp[i - 2] + nums[i], dp[i - 1])
        return dp[-1]
```