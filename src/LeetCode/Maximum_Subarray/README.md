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