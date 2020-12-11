# [Top K Frequent Elements](https://leetcode.com/explore/interview/card/top-interview-questions-medium/110/sorting-and-searching/799/)

> 2020-12-11

정수로 이루어진 배열이 있을 때 가장 빈도수가 높은 정수 값들을 k개 만큼 반환하는 문제입니다.

> ##### Note
> - You may assume k is always valid, 1 ≤ k ≤ number of unique elements.
> - Your algorithm's time complexity must be better than O(n log n), where n is the array's size.
> - It's guaranteed that the answer is unique, in other words the set of the top k frequent elements is unique.
> - You can return the answer in any order.

### solve 1.
먼저 `Counter`라이브러리를 이용해서 배열안에 element들의 수를 기존으로 dictionary를 만든 다음, value를 기준으로 정렬합니다.
그리고 앞에서부터 k만큼 key를 반환합니다.

Counter 라이브러리가 `O(n)`만큼의 time complexity가 요구되고, 
sort 라이브러리가 `O(n log n)`이므로 해당 알고리즘의 토탈 time complexity는 `O(n log n)`이 됩니다.
```python
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        items = sorted(collections.Counter(nums).items(), key=lambda x: x[1], reverse=True)
        return [items[i][0] for i in range(k)]
```