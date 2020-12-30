# [Maximum Product Subarray](https://leetcode.com/problems/maximum-product-subarray/)

> 2020-12-29

숫자로 이루어진 배열이 주어졌을 때, 배열안의 subarray들의 곱이 가장 크게 되는 경우를 찾아서 return하는 문제입니다.

### solve 1.
이 문제는 dynamic programing을 이용해서 풀 수 있습니다.

문저 최소 값을 최적해로 갖는 `mn` 배열과, 최대 값을 최적해로 갖는 `mx` 배열을 선언합니다.
(이때 두 array의 첫번째 값을 `nums`의 첫번째 값으로 채워줍니다.)

그래고 `nums` 배열을 돌게 되면서 `nums[i]` 값과 `mn[i - 1] * cur`, `mx[i - 1] * cur`을 비교하여 `mx`배열과 `mn`배열의 최적해를 채워줍니다.
이렇게 하는 이유는, 두개의 음수 값이 곱해지면 양수 값이 되기 때문에 단순히 `mx`값만을 사용하는 것이 아니라 `mn` 값을 함께 비교하는 것입니다.

for문이 끝나면 `mx` 배열에서 가장 큰 값을 return 해줍니다.

```python
class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        mn = [nums[0]] + [0 for _ in range(1, len(nums))]
        mx = [nums[0]] + [0 for _ in range(1, len(nums))]

        for i in range(1, len(nums)):
            cur = nums[i]
            mn[i] = min(cur, mn[i - 1] * cur, mx[i - 1] * cur)
            mx[i] = max(cur, mn[i - 1] * cur, mx[i - 1] * cur)
        return max(mx)
```