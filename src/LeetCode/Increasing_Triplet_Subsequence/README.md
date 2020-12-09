# [Increasing Triplet Subsequence](https://leetcode.com/submissions/detail/428880768/?from=explore&item_id=781)

> 2020-12-09

**정렬되지 않은** 배열이 주어졌을 때, 배열 안에 임의의 index `i`, `j`, `k`가 `arr[i] < arr[j] < arr[k]`가 되는지 확인하는 문제입니다.

> i, j, k가 순서대로 위치해야 하는 줄 알고 삽질을 했는데, i, j, k의 순서는 상관 없었습니다. 😭
> **문제를 제대로 읽도록 합니다.**

> Note: Your algorithm should run in O(n) time complexity and O(1) space complexity.
>
> - time complexity: `O(n)`
> - space complexity: `O(1)`

### solve 1.
`fir`은 `nums`의 첫번째 element를, `sec`에는 값을 찾아야하므로 최대값을 할당해줍니다.

이제 for문을 돌며 **세번째** 값을 찾게 됩니다. 만약 `num`값이 `sec`보다 크다면, `sec`은 `fir`보다 크므로,
`nums[fir] < nums[sec] < nums[num]`이 성립하기 때문에 `True`를 반환합니다.

만약 `sec`보단 크진 않지만 `fir`보단 크다면, `sec`에 값을 할당해줍니다.
먄약 `fir`보다 `num`이 작다면 현재 나온 값중 최소값이기 때문에 `fir`에 값을 저장해줍니다.

만약 for문이 끝날 때까지 값을 찾지 못했다면 `False`를 return 해줍니다.

```python
class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:
        if len(nums) < 3:
            return False
        fir, sec = nums[0], float('inf')
        for num in nums:
            if num > sec:
                return True
            elif num > fir:
                sec = num
            elif num < fir:
                fir = num
        return False
```