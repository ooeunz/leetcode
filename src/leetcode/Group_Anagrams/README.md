# [Group Anagrams](https://leetcode.com/explore/interview/card/top-interview-questions-medium/103/array-and-strings/778/)

> 2020-12-08

문자열로 이루어진 배열이 주어졌을 때, anagram인 문자열끼리 그룹화하여 배열에 담아 return 하는 문제입니다.

### solve 1.
먼저 default value로 list를 갖는 `ans`라는 딕셔너리를 선언합니다. 
그 후 strs안에 있는 문자들을 하나씩 꺼내서 문자열을 정렬하여 `ans` 딕셔너리에 해당 문자열로 이루어진 key 값이 있다면 
해당 key에 value로 `str`을 추가하고,만약 없다면 새롭게 key를 할당해서 배열에 값을 추가해갑니다.

strs를 모두 순회하였다면 `ans`의 values만을 return합니다.

해당 알고리즘은 `strs`를 한번 순회하기 때문에 `O(n)`만큼의 time complexity와 최대 n만큼의 dictionary 자료구조가 필요하기 때문에 space complexity 역시 `O(n)`입니다.
```python
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        ans = collections.defaultdict(list)
        for str in strs:
            ans[tuple(sorted(str))].append(str)
        return list(ans.values())
```