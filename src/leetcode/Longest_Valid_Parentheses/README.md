# [Longest Valid Parentheses](https://leetcode.com/problems/longest-valid-parentheses/)

현재 알고리즘은 Best practice가 아니므로 풀이를 첨부하지 않습니다.

```java
import java.util.HashSet;
import java.util.Set;

public class Solution {
    public int longestValidParentheses(String s) {
        char OPEN = '(';
        char CLOSE = ')';
        Set<Character> set = new HashSet<>();
        set.add('1');
        set.add('2');
        set.add('L');

        String ss = s.replaceAll("\\(\\)", "L");
        char[] chars = ss.toCharArray();

        for (int i = 0; i < chars.length; i++) {
            if (chars[i] == 'L') {
                chars[i] = '2';

                int start = i - 1;
                int end = i + 1;
                while (inBound(start, end, chars.length)) {
                    while (0 <= start && set.contains(chars[start])) {
                        start--;
                    }
                    while (end < chars.length && set.contains(chars[end])) {
                        end++;
                    }
                    if (inBound(start, end, chars.length) && chars[start] == OPEN && chars[end] == CLOSE) {
                        chars[start--] = '1';
                        chars[end++] = '1';
                        continue;
                    }
                    break;
                }
            }
        }
        return countBracket(chars);
    }

    public int countBracket(char[] chars) {
        int mx = 0;
        int ans = 0;
        for (char c : chars) {
            if (c == '1' || c == '2') {
                mx = c == '1' ? mx + 1 : mx + 2;
                ans = Math.max(mx, ans);
            } else {
                mx = 0;
            }
        }
        return ans;
    }

    public boolean inBound(int start, int end, int size) {
        return 0 <= start && end < size;
    }
}
```