# [Merge Sorted Array](https://leetcode.com/explore/interview/card/top-interview-questions-easy/96/sorting-and-searching/587/)

> 2020-12-01

두개의 정렬된 배열이 주어 졌을 때, 새로운 memory를 할당하지 않고, 정렬하는 알고리즘을 구현하는 문제입니다.

### solve 1.
풀이의 핵심은 두 배열이 정렬이 되어 있다는 것을 이용하는 것입니다.
`num1`을 하나씩 순회하며 지금 순회하고있는 index의 값이 `num2`의 첫번째 값보다 작거나 같으면 계속해서 loop를 돌고,
만약 크다면 두 값을 변경해줍니다.

그런 다음 bubble sort를 이용해서 `nums2`의 첫번째 값으로 들어간 변경된 값을 `nums2`에서 알맞은 자리로 이동시켜줍니다.
이때 `nums2`는 이미 정렬이 되어 있기 때문에, 해당 값의 다음 index보다 작으면 그 다음 값들은 검사할 필요가 없기 때문에 최대 `n`번만으로 index의 위치를 찾을 수 있습니다.

그런 다음 `nums1`의 m 뒤의 값에 `nums2`를 넣어주도록 합니다.

이 풀이에서 time complexity는 `nums1`의 길이인 `m`만큼 `nums2`의 첫번째 index와 비교해야하고, 이후에 값을 교환한다면 `nums2`를 정렬해주어야하기 때문에 `O(mn)`이라고 할 수 있습니다.
또한 여분의 memory를 할당하지 않았기 때문에 space complexity는 `O(1)`입니다.

```python
class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        if nums2:
            for i in range(m):
                if nums1[i] > nums2[0]:
                    nums1[i], nums2[0] = nums2[0], nums1[i]
                    for j in range(n - 1):
                        if nums2[j] > nums2[j + 1]:
                            nums2[j + 1], nums2[j] = nums2[j], nums2[j + 1]
            for i in range(n):
                nums1[m] = nums2[i]
                m += 1
``` 