# [Sorting and Searching](https://leetcode.com/explore/interview/card/top-interview-questions-easy/96/sorting-and-searching/774/)

> 2020-12-01

`isBadVersion(version)` 함수를 호출 했을 때 가장 처음 `True`를 반환하는 index를 찾는 문제입니다.
 가장 앞에 있는 `True` 이후로 모든 index는 `True`인 상태입니다.
 
 ### solve 1.
 가장 쉬운 풀이는 처음부터 끝까지 하나씩 값을 조회하면서 `True`인 값이 나올 경우 해당 index를 return하는 방법입니다.
 이러한 경우 하나의 배열을 모두 탐색해야하기 때문에 time complexity가 `O(n)`만큼 나오게 됩니다.
 
 문제에서 주어진 배열의 범위가 최대 `2^31 - 1`이기 때문에 이와같이 완전탐색을 하게 될 경우 time error가 나기 쉽습니다.
 
 > 보통 이런 문제는 완전 탐색을 하는 경우 time error가 발생합니다.
 ```python
class Solution:
    def firstBadVersion(self, n):
        for i in range(n):
            if isBadVersion(i):
                return i
        return n
```

### solve 2.
두번째 방법은 **첫번째 `True` 이후의 index는 모두 `True`라는 rule을 이용**해서, 이분 탐색을 하는 방법입니다.
시작점과 끝점을 기준으로 중간 값 `mid`을 확인했을 때 `False`라면 `start = mid + 1`을 하고 (`mid`값은 이미 확인 했으므로)
`True`라면 `end = mid - 1`을 해서 탐색 범위를 좁혀갑니다. 

결과적으로 반복문이 끝나게 되면 `start`는 가장 처음에 위치한 `True`가 있는 index를 가리키게 됩니다.
> 만약 이 부분이 이해가 되지 않는다면 0은 `False` 1은 `True`인 예시를 생각해봅니다.
> `(0 + 1) // 2 = (start + end) // 2 = 0`으로 `mid` 값은 `0`을 가리키게 되고, 
>`mid`값이 `False`임에 따라 `start = mid + 1`을 하게 되므로 결과적으로 `start`는 가장 처음에 있는 `True`를 가리키게 됩니다.

이분탐색을 하게 되는 경우 매번 탐색시 마다 범위가 `1/2`로 줄어들기 때문에 time complexity가 `O(logN)`으로 매우 빠른 시간으로 탐색할 수 있습니다.

```python
class Solution:
    def firstBadVersion(self, n):
        start, mid, end = 0, 0, n
        while start <= end:
            mid = (start + end) // 2
            if isBadVersion(mid) is False:
                start = mid + 1
            else:
                end = mid - 1
        return start
```