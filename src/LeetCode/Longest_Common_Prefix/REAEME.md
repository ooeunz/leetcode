# [Longest Common Prefix](https://leetcode.com/explore/interview/card/top-interview-questions-easy/127/strings/887/)

> 2020-11-29

배열안에 있는 문자들의 공통적으로 가장 긴 prefix를 찾는 문제입니다.

### solve 1.
이 알고리즘을 푸는 가장 핵심적인 개념 중 하나는 **가장 짧은 문자열과 그 다음으로 긴 문자열을 비교했을 때 `False`라면 이후의 문자열은 비교할 필요가 없다.** 라는 것입니다.

그렇기 때문에 배열안의 문자열들을 짧은 순서대로 정렬하고, 첫번째 문자열의 길이를 일부씩 `.startswith()`하며 뒤의 문자열들과 비교합니다.

그런데 만약 이후의 prefix `False`가 아닌 경우가 있다면 이후의 문자열들을 검사하지 않아도 `False`이기 때문에 `return ans`를 해줍니다.
```python
class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if not strs:
            return ""
        ans = ""
        strs.sort(key=lambda x: len(x), reverse=True)
        firstString = strs[0]
        for i in range(len(firstString) + 1):
            for idx, str in enumerate(strs):
                if not str.startswith(firstString[:i]):
                    return ans
                elif str.startswith(firstString[:i]) and idx == len(strs) - 1:
                    ans = firstString[:i]
        return ans
```