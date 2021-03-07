package LeetCode.Palindrome_Number;

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

    public static void main(String[] args) {
        Solution solution = new Solution();

        System.out.println(solution.isPalindrome(101));
        System.out.println(solution.isPalindrome(-101));
    }
}