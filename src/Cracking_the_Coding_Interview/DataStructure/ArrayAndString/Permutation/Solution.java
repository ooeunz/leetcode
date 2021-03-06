package Cracking_the_Coding_Interview.DataStructure.ArrayAndString.Permutation;

public class Solution {
    public boolean isPermutation(String str, String compareStr) {
        if (str.length() != compareStr.length()) {
            return false;
        }
        int[] letters = new int[128];

        char[] charArr = str.toCharArray();
        for (char c : charArr) {
            letters[c]++;
        }
        for (int i = 0; i < compareStr.length(); i++) {
            int val = compareStr.charAt(i);
            letters[val]--;
            if (letters[val] < 0) {
                return false;
            }
        }
        return true;
    }

    public static void main(String[] args) {
        Solution solution = new Solution();

        System.out.println(solution.isPermutation("asdf", "sdfa"));
    }

}
