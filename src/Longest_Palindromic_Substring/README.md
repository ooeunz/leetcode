[Solving Longest_Palindromic_Substring](https://leetcode.com/problems/longest-palindromic-substring/)

> 2020-11-09

앞뒤로 뒤집어도 같은 문자열이 되는 가장 긴 문자열을 찾는 문제입니다. 과
문제를 풀었던 핵심적인 아이디어는 **뒤집어도 같은 문자열은 맨 처음과 맨 끝의 문자가 같다**라는 점과 
start와 end pointer를 기준으로 문자열의 길이가 현재까지 찾은 palindromic string의 길이보다 큰 경우에만 palindromic 여부를 확인함으로써 연산 수를 줄이는 방법입니다.

해당 알고리즘은 최악의 경우 `O(n)^2`만큼의 time complexity를 가지게 됩니다.
또한 중복되는 문자들의 index를 저장하는 dictionary가 필요하므로 space comflexity 역시 `O(n)^2`만큼 필요합니다.

### solve 1.
먼저 문자열에 있는 모든 문자를 key 값으로 하는 `{문자: []}`형태의 dictionary를 만들어줍니다.
그리고 문자를 하나씩 찾을 때마다 dictionary에 해당 문자의 index를 push해주고 안에 있는 index들을 조합하여 **길이가 가장 길면서 뒤집어도 같은 문자열을 찾아서 ans와 mx에 저장하며 정답을 찾습니다.**
```python
class Solution:
    def longestPalindrome(self, s: str) -> str:
        mx = 0
        ans = []
        dic = {val: [] for val in set(s)}
        for i, val in enumerate(s):
            dic[val].append(i)
            for j in range(len(dic[val])):
                start = dic[val][j]
                end = dic[val][-1] + 1
                if end - start > mx and s[start:end] == ''.join(reversed(s[start:end])):
                    mx = end - start
                    ans = [start, end]
        return s[ans[0]:ans[1]]
```