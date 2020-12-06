# [Maximum Subarray](https://leetcode.com/explore/interview/card/top-interview-questions-easy/97/dynamic-programming/566/)

> 2020-12-06

배열이 주어졌을때 배열의 연속된 부분합이 가장 큰 값을 return 하는 문제입니다.

### solve 1.
가장 간단한 방법은 brute force로 모든 경우의 수의 합을 구하는 방법입니다. 하지만 주어진 배열의 모든 경우의 수를 구해야하기 때문에
time complexity가 `O(n^2)`으로 time error가 발생하게 됩니다.
```python
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        length = len(nums)
        if length == 0:
            return 0
        mx = float('-inf')
        for i in range(length):
            for j in range(i + 1, length + 1):
                mx = max(mx, sum(nums[i:j]))
        return mx
```

### solve 2.
두번 째 방법은 아래의 규칙을 활용한 방법입니다.
- 더한 값이 **음수**일 경우 다음 값을 더해도 값이 **음수**입니다. 
    - 때문에, 배열의 부분의 시작점이 음수로 시작하거나 합이 음수라면 처음부터 start 포인트를 초기화해야합니다.
- 더한 값이 **양수**라면 앞으로 값이 더 커질 수 있으므로 계속해서 값을 더해갑니다.

위의 조건에 의해 만들어진 아래의 알고리즘은 만약 음수로만 이루어진 배열이 들어올 경우 매번 `sub_sum` 값을 초기화 하기 때문에
더한 값을 누적하지 않고, 매번 탐색하는 index의 값에 한해서만 `ans`와 `max()`연산을 하게됩니다.
 
sovle 1.과 달리 solve 2.은 n번만큼의 loop를 돌기 때문에 `O(n)`의 time complexity를 가지게됩니다.

```python
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0
        ans = nums[0]
        sub_sum = 0
        for num in nums:
            sub_sum += num
            ans = max(ans, sub_sum)
            if sub_sum < 0:
                sub_sum = 0
        return ans
```