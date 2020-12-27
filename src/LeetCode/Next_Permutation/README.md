# [Next Permutation](https://leetcode.com/problems/next-permutation/)

> 2020-12-26

배열안에 정수가 주어 졌을 때, 다음 permutation으로 배열안의 element들의 순서를 변경하는 문제입니다.
만약 주어진 배열이 마지막 permutation (예를들면 `[3, 2, 1]`)이라면 첫번째 permutation (`[3, 2, 1]` -> `[1, 2, 3]`)으로 변경합니다.

### solve 1.
이 문제는 permutation을 generate 함수는 backtracking을 이용한다는 사실을 알고 있어야 합니다.
그에 따르면 `[2, 4, 3, 1]`와 같은 permutation 배열은 descending array 앞의 값인 
`2`가 desending array에서 `2` 다음으로 큰 값인 `3`과 바뀐 후, 
reverse 된다는 reverse 된다는 패턴을 찾을 수 있습니다.

순서대로 표현하자면 아래와 같습니다.
1. `[2, 4, 3, 1]`   # 바뀌기 전
2. `[3, 4, 2, 1]`   # `2와 `3` 변경
3. `[3, 1, 2, 4]`   # descending array를 reverse

풀이를 코드로 작성하면 아래와 같습니다.

```python
class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        decrease_section = next_large = len(nums) - 1
        while decrease_section > 0 and nums[decrease_section - 1] >= nums[decrease_section]:
            decrease_section -= 1
        if decrease_section == 0:
            nums.reverse()
            return

        pivot = decrease_section - 1
        while nums[pivot] >= nums[next_large]:
            next_large -= 1
        nums[pivot], nums[next_large] = nums[next_large], nums[pivot]

        def reverse_lst(lst: list, start, end):
            while start < end:
                lst[start], lst[end] = lst[end], lst[start]
                start += 1
                end -= 1
        reverse_lst(nums, pivot + 1, len(nums) - 1)
```