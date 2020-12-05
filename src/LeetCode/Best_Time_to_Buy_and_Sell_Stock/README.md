# [Best Time to Buy and Sell Stock](https://leetcode.com/explore/interview/card/top-interview-questions-easy/97/dynamic-programming/572/)

> 2020-12-05

주식 가격이 배열로 주어질 경우 가장 비싸게 주식을 팔았을 때의 이익을 return하는 문제입니다.

### solve 1.
시작은 배열의 가장 마지막 index에 주식을 파는 것을 기준으로 합니다. 그리고 앞으로 하나씩 index를 옮겨가며 주식을 사는 날짜를 찾는 알고리즘입니다.
index가 움직일 때마다 `end - prices[i]`와 현재까지 가장 비싸게 판 가격과 비교합니다.

그리고 만약 `end`보다 현재 index의 값이 더 크다면 `end`의 값을 변경해줍니다.
이러한 방법은 one pass로 정답을 찾을 수 있기 때문에 time complexity가 `O(n)`이고, 다른 배열이나 자료구조를 사용하지 않으므로 space complexity 역시 `O(1)`입니다.
```python
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if not prices:
            return 0
        end = prices[-1]
        mx = 0
        for i in range(len(prices) - 1, -1, -1):
            mx = max(end - prices[i], mx)
            if prices[i] > end:
                end = prices[i]
        return mx
```