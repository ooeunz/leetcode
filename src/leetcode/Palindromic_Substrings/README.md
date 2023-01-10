# [Palindromic Substrings](https://leetcode.com/problems/palindromic-substrings/submissions/)

> 2020-12-09

문자열이 주어 졌을 때 해당 문자열에 palindromic인 문자열이 몇개 있는지 찾는 문제입니다.

### solve 1.
가장 간단하게 문제를 푸는 방법은 brute force로 모든 경우의 수를 탐색하는 방법입니다.
for문을 두개 중첩해서 선택한 부분 문자열이 거꾸로해도 같은지를 확인하고 만약 같다면 `ans`의 값을 1올립니다.
 
그리고 중첩 for문이 종료되면 return합니다.

이러한 경우 time complexity는 `O(n^2)`입니다.

> java
```java
public class Solution {
    public int countSubstrings(String s) {
        int ans = 0;

        for (int i = 0; i < s.length(); i++) {
            for (int j = i + 1; j < s.length() + 1; j++) {
                String slice = s.substring(i, j);
                StringBuilder compare = new StringBuilder(slice);
                if (slice.equals(compare.reverse().toString())) {
                    ans++;
                }
            }
        }
        return ans;
    }
}
```

> python
```python
class Solution:
    def countSubstrings(self, s: str) -> int:
        ans = 0
        for i in range(len(s)):
            for j in range(i + 1, len(s) + 1):
                compare = s[i:j]
                if compare == compare[::-1]:
                    ans += 1
        return ans
```