[Merge Intervals](https://leetcode.com/explore/interview/card/top-interview-questions-medium/110/sorting-and-searching/803/)

> 2020-12-11

2차원 배열이 주어졌을 element로 들어있는 또 하나의 배열의 각 요소들은 배열의 index를 나타냅니다.
이때 범위가 중첩되는 모든 배열을 합치는 문제입니다.

예를들어 `[1, 3], [2, 6]]`와 같은 배열이 있다면 `[1, 6]`으로 합쳐집니다.

### solve 1.
먼저 첫번째 element를 기준으로 `intervals`배열을 정렬합니다.
그런 다음 for문을 돌며 배열의 요소들을 검사하게 되는데, 앞 직전의 배열과 뒤의 배열이 merge할 수 있는지를 확인하기 위해,
첫번째 배열 두번째 요소와 두번째 배열의 첫번째 요소의 값의 크기를 비교합니다.

예를 들어 `[1, 3], [2, 6]]`라면, `3`과 `2`를 비교하여, 3이 더 크기 때문에 두 배열을 merge할 수 있습니다.
merge할때는 첫번째 element를 기준으로 정렬되었기 때문에 첫번째 배열의 첫번째 값을 `start`로, 그리고 두번째 값은 두 배열의 두번째 element를 비교하여 큰 값을 넣어줍니다.

만약 merge가 가능하다면 `ans`배열의 가장 끝의 element를 대체하게 되고, 이후에 `ans`배열의 마짐가 요소를 이용해 다시 비교하게 됩니다.
하지만 merge가 불가능하다면 단순히 `intervals`배열의 element를 `ans`에 추가해줍니다.

해당 알고리즘의 time complexity는 `O(n log n)`입니다.
```python
class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        if not intervals:
            return []
        intervals.sort(key=lambda x: x[0])
        ans = [intervals[0]]
        for i in range(1, len(intervals)):
            fir = ans[-1]
            sec = intervals[i]
            if fir[1] >= sec[0]:
                ans[-1] = [fir[0], max(fir[1], sec[1])]
            else:
                ans.append(sec)
        return ans
```