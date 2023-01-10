# [3Sum](https://leetcode.com/explore/interview/card/top-interview-questions-medium/103/array-and-strings/776/)

> 2020-12-07

배열이 주어졌을 때 배열안의 3개의 수를 조합해서 `0`이 나오는 조합을 모두 구하여 return 하는 문제입니다.

### solve 1.
먼저 주어진 배열을 정렬합니다. 그럼 다음 배열을 탐색하게 될텐데 기본적인 컨셉은 아래와 같습니다.
```markdown
[0, 1, 1, 2, 2, 3, 4, 5]
[i][left]            [right] 
```
`i`를 기준으로 오른쪽에 있는 two pointer `left`와 `right`를 이동해가며 합이 0이되는 값을 찾는 것 입니다.
만약 합이 0보다 작다면 `left`를 오른쪽으로 이동합니다. 왜냐하면 배열은 정렬되어 있기 때문에 오른쪽으로 이동할 수록 합이 커지기 때문입니다.
또한 마찬가지로 만약 합이 0보다 크다면 `right`를 왼쪽으로 이동합니다.

만약 합이 0이되는 값을 찾는다면 `ans`에 값을 추가하고, `left`와 `right`를 같은 수가 아닌 다음 수부터 탐색 할 수 있도록 이동합니다.
이를테면 위의 예시 배열에서 `left`가 1을 가리키고 있다면, 1에 해당하는 값을 `ans`에 담았기 때문에 while문을 이용해 (배열에 1이 여러개 이므로) 2에 위치하도록 이동시켜줍니다.

```python
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        ans = []
        for i in range(len(nums) - 2):
            if i > 0 and nums[i - 1] == nums[i]:
                continue
            left, right = i + 1, len(nums) - 1
            while left < right:
                sum_num = nums[i] + nums[left] + nums[right]
                if sum_num < 0:
                    left += 1
                elif sum_num > 0:
                    right -= 1
                else:
                    ans.append([nums[i], nums[left], nums[right]])
                    while left < len(nums) - 1 and nums[left + 1] == nums[left]:
                        left += 1
                    while right > 0 and nums[right - 1] == nums[right]:
                        right -= 1
                    left += 1
                    right -= 1
        return ans
```