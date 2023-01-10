package leetcode.Palindromic_Substrings;

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

    public static void main(String[] args) {
        Solution solution = new Solution();

        // Check answer.
        System.out.println(solution.countSubstrings("abc") == 3);
        System.out.println(solution.countSubstrings("aaa") == 6);
    }
}
