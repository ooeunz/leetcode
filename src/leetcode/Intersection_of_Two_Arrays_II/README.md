# [Intersection of Two Arrays II](https://leetcode.com/explore/interview/card/top-interview-questions-easy/92/array/674/)

> 2020-11-28

[Single Number](./../Single_Number)의 연속된 문제로 이번엔 두개의 배열에 둘 다 존재하는 수를 list형태로 반환하는 문제입니다.
> 처음엔 문제를 잘못 읽어서 nums1이나 nums2가 가장 길게 연속되는 길이를 구하는 문제인 줄 알았다. 문제를 더 잘 읽도록 하자...😭

### solve 1.
이 문제도 Counter library를 사용하면 쉽게 풀 수 있는 문제입니다. 먼저 nums1을 Counter로 만들어 준 다음, 
nums2 배열을 하나씩 순환하며,해당 수(`num`)가 cnt의 key값으로 존재하고, 0이 아닐 경우 `ans` 배열에 값을 추가해줍니다. 
그리고 같은 수라도 여러 개 있을 수 있기 때문에 `cnt[num] -= 1` nums1에 있는 해당 `num`의 수를 줄여줍니다.

```python
class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        ans = []
        cnt = Counter(nums1)
        for num in nums2:
            if num in cnt and cnt[num] > 0:
                ans.append(num)
                cnt[num] -= 1
        return ans
``` 