# [보석 쇼핑](https://programmers.co.kr/learn/courses/30/lessons/67258)

`gems` 배열에 보석의 이름들이 주어 졌을 때, 모든 보석을 포함할 수 있는 가장 짧은 범위를 return 하는 문제입니다.

> 2020-01-17

해당 문제는 Brute Force로 풀게 될 경우, TLE가 쉽게 발생하는 문제로, 투 포인터 알고리즘을 이용해서 풀 수 있습니다.
1. 0부터 시작해서 모든 보석들이 포함될때까지 `end`를 옮깁니다.
2. 모든 보석을 포함하게 되면 `start`를 옮기면서 모든 범위를 포함할 수 있는 최소의 범위를 찾습니다.
3. 1번과 2번을 반복합니다.

```python
import collections


def solution(gems):
    start = end = 0

    GEMS_LENGTH = len(gems)
    GEMS_NUMS = len(set(gems))

    bag = collections.defaultdict(int)
    ans = [1, GEMS_LENGTH]

    bag[gems[start]] += 1
    while start < GEMS_LENGTH and end < GEMS_LENGTH:
        if len(bag) == GEMS_NUMS:
            if bag[gems[start]] == 1:
                ans = min([ans, [start + 1, end + 1]], key=lambda x: x[1] - x[0])
                del bag[gems[start]]
            else:
                bag[gems[start]] -= 1
            start += 1
        else:
            end += 1
            if end == GEMS_LENGTH:
                break
            bag[gems[end]] += 1
    return ans
```