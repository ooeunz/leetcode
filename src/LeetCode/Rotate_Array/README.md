# [Rotate Array](https://leetcode.com/problems/rotate-array/)

> 2020-11-22

이 문제 역시 space complexity를 O(1)을 유지해야하는 문제입니다. 기존의 코딩테스트는 주로 time complexity만을 고려해서 풀어왔기 때문에 이런 문제에 대해서는 조금 익숙하지 않았습니다.

만약 space complexity의 제한이 없다면 아래와 같이 쉽게 rotate를 구현할 수 있습니다.

```python
class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        nums = nums[k:] + nums[:k]
```

### solve 1.
문제에도 이 알고리즘을 풀 수 있는 방법이 최소 3가지 이상이라고 나와있는데, 가장 쉽게 풀 수 있는 방법은 역시 `Brute Force`입니다.
```python
class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        for i in range(k):
            previous = nums[-1]
            for j in range(len(nums)):
                nums[j], previous = previous, nums[j]
``` 

space complexity를 O(1)로 맞추기 위해 nums의 가장 마지막 index를 마치 temp처럼 사용하여 rotate에 따른 값을 교환해줍니다.
Brute Force의 경우 time complexity는 `O(n + k)`입니다.

해당 알고리즘을 사용할 경우 leetcode에서 **Time Limit Exceeded**을 만나게 됩니다.  