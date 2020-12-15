# [Find All Numbers Disappeared in an Array](https://leetcode.com/problems/find-all-numbers-disappeared-in-an-array/submissions/)

> 2020-12-15

정수로 이루어진 배열이 주어집니다. 해당 배열엔 두개의 같은 정수가 있거나 하나의 정수가 있습니다.
이때 1부터 배열안의 가장 큰 정수까지 중에 없는 수를 return하는 문제입니다.

### solve 1.
이 문제의 포인트는 아래와 같습니다.
- 정렬되어있진 않지만, 배열안의 정수들의 값이 이어진다.
- 배열의 총 길이는 배열안에 가장 큰 수와 동일하다.

이와 같은 특성을 이용해서 배열을 순환하면서 현재 방문하고 있는 `idx`의 값을 다시 `idx`와 일치시키는 것입니다.
즉 `nums[idx]`이 `nums[nums[idx] - 1]`에 가도록 하는 것입니다. (여기서 `-1`을 하는 이유는 배열이 0부터 시작하고, 문제 조건상 추가적인 index를 할당 할 수 없기 때문입니다.)

모든 값들이 올바른 index값에 가도록 배열을 한번 순환한 후엔, index와 value가 일치하지 않는 것들을 `ans`에 담아서 return 해줍니다.
해당 알고리즘은 time complexity가 `O(n)` space complexity가 `O(1)`입니다.

```python
class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        idx = 0
        ans = []
        while idx < len(nums):
            val = nums[idx]
            if nums[idx] != nums[val - 1]:
                nums[idx], nums[val - 1] = nums[val - 1], nums[idx]
            else:
                idx += 1
        for i, v in enumerate(nums):
            if i != v - 1:
                ans.append(i + 1)
        return ans
```

### solve 2.
두번 째는 집합 자료구조를 사용하는 방법입니다. 
1부터 n까지의 온전한 값이 존재하는 `set`자료형과 `set(nums)`의 차집합을 구하는 것입니다.

```python
class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        return list(set(range(1, len(nums) + 1)) - set(nums))
```