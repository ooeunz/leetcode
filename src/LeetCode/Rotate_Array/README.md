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

### solve 2.
두번째 방법은 조금 생각의 전환을 해보는 방법입니다. 오른 쪽으로 ratate가 될 때마다 우측 끝 value가 왼쪽 끝으로 이동한다는 점을 이용해서 배열 전체를 reverse하는 방법입니다.
배열 전체를 reverse 한 이후 k를 기준으로 다시 reverse를 시켜줍니다.

이 때 주의할 점은 배열의 길이가 k보다 작은 경우 out of index가 발생할 수 있기 때문에 `k %= n`으로 n보다 k가 클 경우엔 n번 만큼만 수행하도록 합니다. 
(배열의 길이를 여러 번 순회하는 걸 한번만 하도록 나머지 연산을 해줍니다. 이와 같이 나머지 연산을 이용하여 알고리즘의 연산 수를 획기적으로 줄일 수 있는 경우가 많으니 기억해둡니다.)
```python
class Solution:
    def reverse(self, nums: list, start: int, end: int):
        while start < end:
            nums[start], nums[end] = nums[end], nums[start]
            start += 1
            end -= 1

    def rotate(self, nums: List[int], k: int) -> None:
        n = len(nums)
        k %= n
        
        self.reverse(nums, 0, n - 1)
        self.reverse(nums, 0, k - 1)
        self.reverse(nums, k, n - 1)
```