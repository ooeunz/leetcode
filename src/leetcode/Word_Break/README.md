# [Word Break](https://leetcode.com/problems/word-break/submissions/)

> 2020-01-08

주어진 문자열 `s`를 문자열로 이루어진 list `wordDict`의 요소들을 이용해서 2개 이상으로 나눌 수 있는지 확인하는 문제입니다.
예를들어 `s = "leetcode", wordDict = ["leet", "code"]` 라면 `s`는 `leet`와 `code`로 나눌 수 있습니다.

`wordDict`에 있는 문자열은 여러번 재사용 할 수 있습니다.

### solve 1.
먼저 이 문제는 백트래킹을 이용해서 시도할 수 있습니다.

문자열을 나누어가며 wordDict안에 있는 문자열이 substring인지 확인하고 맞다면 해당 부위를 제외하고 `s`문자열을 slice하여 재귀적으로 확인합니다.
하지만 이와 같이 풀이할 경우 **Time Limit Exceeded**가 발생하게 됩니다.

```python
class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        def backtracking(ss: str):
            if not ss:
                return True
            for word in wordDict:
                if ss.startswith(word):
                    if backtracking(ss[len(word):]):
                        return True

        for word in wordDict:
            if s.startswith(word):
                if backtracking(s[len(word):]):
                    return True
        return False
```

### solve 2.
두번째 풀이는 dynamic programing을 이용하는 방법입니다.
문자열 `s`와 동일한 크기의 `dp`배열을 선언해줍니다. 

여기서 `dp`배열의 각 요소는 `wordDict`의 문자열이 시작할 수 있는 최적해를 나타냅니다.
`dp`배열의 `dp[i]`는 `dp[lastTrue:i]`와 같이 마지막 `True`부터 `i`이전까지 subString이 유효하다는 것을 나타냅니다.

예를들어 `s = "leetcode", wordDict = ["leet", "code"]`인 경우, 
`s[0].startswith(wordDict[0])) is True`이기 때문에 `dp[0 + len(wordDict[0])] = True`가 됩니다.
따라서 `dp[0 + len(wordDict[0])]`에서 다시 `wordDict`의 값들이 subString인지 확인하며 `dp`배열의 최적해를 채워나갈 수 있습니다.

이와 같이 `dp`의 값이 `True`인 것들만 확인해 나가며, `i + len(word)`와 `s`문자열의 길이가 같다면 
해당 문자열은  `wordDict`의 요소들로 나눌 수 있는 것이 확인이 되기 때문에 `True`를 return합니다.

반면 `s` 문자열을 모두 순환할 동안 정답이 될 case를 찾지 못하면 `False`를 return 해줍니다.

이렇게 dynamic programing을 이용해서 문제를 풀게 될 경우 해당 알고리즘의 time complexity는 `O(len(s) * len(wordDict))`입니다.
```python
class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        dp = [1] + [0] * (len(s) - 1)
        for i in range(len(s)):
            if dp[i]:
                for word in wordDict:
                    if s[i:].startswith(word):
                        if i + len(word) == len(s):
                            return True
                        elif i + len(word) < len(s):
                            dp[i + len(word)] = 1
        return False
```