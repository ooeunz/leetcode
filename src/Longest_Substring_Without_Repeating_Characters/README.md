# [Longest_Substring_Without_Repeating_Characters](https://leetcode.com/problems/longest-substring-without-repeating-characters/)

> 2020-11-03

주어지는 문자열 중에 가장 길게 연속되지 않는 문자열을 찾는 문제입니다. 알고리즘 자체도 고민을 많이 했지만, 문제를 의도와 다르게 이해하는 실수를 종종 했던 문제입니다.

### solve 1.
알고리즘 구현에는 two pointer 알고리즘을 사용했습니다. 문자열의 길이가 2보다 작다면 문자열의 길이를 return 했고,
뒤에 있는 pointer end가 문자열을 끝까지 순회할동안 loop를 실행합니다. 

기본적으로 end가 한칸씩 뒤로가게되며 `s[start:end]`에 해당하는 문자열을 `Set` 자료형에 저장하고 다음 문자열이 이전에 방문했던 문자열 중 중복이 있는지를 확인합니다.

만약 문자열이 있다면 start pointer가 가리키고 있는 문자열 `s[start]`를 제거하고 start를 +1 해줍니다. 이를 반복해서 `s[start:end]`가 `Set`에 없을 때까지 반복한 후, 지금까지 발견했던 문자열 중 가장 긴 길이를 저장해둔 `mx` 변수의 값과 비교하여 최댓값을 갱신해줍니다.

이와 같은 방법으로 max 길이를 갱신하는 것을 목표로 계속해서 새로운 문자열을 찾고, 전체 문자열을 모두 순회한 경우 `mx` 값을 return해 줍니다. 
```python
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) < 2:
            return len(s)
        start = 0
        end = 1
        pkg = set(list(s[start:end]))
        mx = len(pkg)
        while end < len(s):
            while s[end] in pkg:
                pkg.remove(s[start])
                start += 1
            if start >= end:
                pkg.add(s[start])
                end += 1
            elif s[end] not in pkg:
                pkg.add(s[end])
                mx = max(mx, len(pkg))
                end += 1
        return mx
```