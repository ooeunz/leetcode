# [Permutation](https://leetcode.com/explore/interview/card/top-interview-questions-medium/109/backtracking/795/)

> 2020-12-18

주어진 배열을 이용해서 permutation을 구현하는 문제입니다.

### solve 1.
python에는 permutation을 구현해주는 library가 존재하기 때문에 간단하게 한줄 코드로 구현할 수 있습니다.

```python
from itertools import permutations


class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        return list(map(lambda x: list(x), permutations(nums, len(nums))))
```

### solve 1.
두번 째 방법은 `itertools.permutation`을 사용하지 않고 직접 permutation을 구현하는 방법입니다.

먼저 정답을 담을 `ans`배열과 해당 index의 수를 사용했다는 의미로 사용될 `used`배열을 선언합니다.
그런 다음 실제로 permutation을 생성할 함수인 `generate` 함수를 생성합니다.

`chosen`배열은 실제로 permutation을 만들어서 담는 배열입니다. 
즉 `chosen`배열의 길이와 `nums`의 길이가 같다면 하나의 순열이 다 만들어 진 것이기 때문에 해당 값을 `ans`에 추가해줍니다.
> 여기서 `ans.append(chosen[:])`과 같이 담는 이유는, python에선 배열이 mutable 객체이기 때문에 단순히 
> `chosen`을 넣으면 다른 곳에서 배열의 값이 변경됐을 때 `ans`안에 있는 값도 변경되기 때문입니다.

이후 `nums`의 길이만큼 index를 순환하게 되는데, 만약 해당 index가 사용하지 않았다면 (`if not used[i]`)
`chosen`에 해당 값을 추가하고, 사용했다는 의미로 `used[i] = True`로 만들어줍니다.

그리고 여기 까지 used한 값을 기준으로 모든 permutation을 구하기 위해 재귀를 수행해줍니다.
재귀를 탈출하게 되면 `used[i] = False`를 해주고 계속해서 for문을 돌게됩니다.

`generate`함수가 모두 끝나게되면 `ans`에 담긴 값을 return 합니다.

```python
class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        ans = []
        used = [False] * len(nums)

        def generate(chosen, used):
            if len(chosen) == len(nums):
                ans.append(chosen[:])
            for i in range(len(nums)):
                if not used[i]:
                    chosen.append(nums[i])
                    used[i] = True
                    generate(chosen, used)
                    used[i] = False
                    chosen.pop()
        generate([], used)
        return ans
```