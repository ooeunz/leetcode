# [Container With Most Water](https://leetcode.com/problems/container-with-most-water/)

> 2020-12-13

container의 높이가 배열의 element로 있는 배열이 주어 졌을 때, 최대한 물을 많이 담을 수 있는 용량을 return하는 문제입니다.

### solve 1.
이 문제를 풀 때 핵심적인 조건은
1. 둘 중 높이가 낮은 container 기준으로 물의 높이가 측정된다.
2. 물을 담는 길이의 폭이 긴 것이 무조건 정답이 되진 않는다. 길이는 짧더라도, 높이가 높은 경우가 정답이 될 수도 있다.

위의 조건을 요약하자면, 좌우의 container 중 높이가 낮은 container의 높이가 최대한 높으면서 좌우 container가 최대한 떨어진 경우를 구합니다.

two pointer 알고리즘을 사용해 `left` pointer와 `right` pointer 중 값이 작은 포인터를 이동해가며 최댓값을 찾습니다.
포인터가 이동하면 `min(height[start], height[end]) * abs(end - start)`와 같이 `left`와 `right` 중 작은 값을 구한 후 물의 양을 구합니다.

```python
class Solution:
    def maxArea(self, height: List[int]) -> int:
        start, end = 0, len(height) - 1
        mx = float('-inf')
        while start < end:
            mx = max(mx, min(height[start], height[end]) * abs(end - start))
            if height[start] < height[end]:
                start += 1
            else:
                end -= 1
        return mx
```