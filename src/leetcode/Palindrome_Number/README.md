# [Palindrome Number](https://leetcode.com/problems/palindrome-number/)

주어진 정수가 palindrome인지 확인하는 알고리즘입니다.
정수를 문자 배열로 변환한 후 배열의 시작과 끝에서 출발하여 배열 중앙 방향으로 각 element의 값을 비교합니다.
만약 while문을 탈출할 때까지 다른 문자가 없다면 `true`를 반환합니다.

```java
public class Solution {
    public boolean isPalindrome(int x) {
        char[] s = String.valueOf(x).toCharArray();
        int start = 0;
        int end = s.length - 1;

        while (start < end) {
            if (s[start++] != s[end--]) {
                return false;
            }
        }
        return true;
    }
}
```