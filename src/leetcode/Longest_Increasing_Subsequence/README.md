# [Longest Increasing Subsequence](https://leetcode.com/explore/interview/card/top-interview-questions-medium/111/dynamic-programming/810/)

> 2020-12-16

정수로 이루어진 배열이 주어졌을 때, 가장 긴 부분 수열의 길이를 return 하는 문제입니다.

### solve 1.
해당 문제는 dynamic programing으로 풀 수 있습니다.
먼저 `nums`와 동일한 길이의 `dp` 배열을 만들어줍니다. `dp`배열의 각 element는 해당 index까지의 부분 수열의 길이입니다.
또한 각 element에서 수열이 시작하는 경우를 가정해, 배열은 초기 값은 모두 `1`로 초기화해줍니다.

이제 `nums` 배열을 순환하며 수열을 찾게됩니다. 알고리즘의 기본 컨셉은 `nums`배열에서 `i` 값이 하나 증가할 때마다, 이전의 index들을 순회하는 `j` index의 값과 비교합니다.
만약 이전의 `nums[j]` 값보다 `nums[i]`의 값이 크다면, `dp`배열에서 이전 `dp[j] + 1`, 즉 이전 `j` index까지의 부분 수열의 길이에 `i` index가 하나 추가되는 값과, `dp[i]`를 비교하여 큰 값을 `dp[i]`에 넣어줍니다.

여기서 `dp[i]`에는 처음에는 `1`이 들어있겠지만, 이후에 `dp[j] + 1`과 `dp[i]`를 여러 번 비교하게 된다면 `i`가 수열에 추가될 수 있는 최대의 길이를 `dp[i]`에 저장하게 됩니다.
이렇게 `nums`길이만큼 반복문을 순회하며 `dp` 배열안의 가장 큰 값을 return 합니다.

해당 알고리즘은 `nums`배열을 순환하며 동시에 각 index에 대해 이전의 index들을 다시 한번 순환하기 때문에 time complexity가 `O(n^2)`입니다.
그리고 `nums`의 길이만큼 추가 메모리를 사용하므로 space complexity는 `O(n)`이라고 할 수 있습니다.
```python
class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        dp = [1] * len(nums)
        mx = 1
        for i in range(len(nums)):
            for j in range(i):
                if nums[j] < nums[i]:
                    dp[i] = max(dp[j] + 1, dp[i])
                    mx = max(mx, dp[i])
        return mx
```