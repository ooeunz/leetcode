package Cracking_the_Coding_Interview.DataStructure.ArrayAndString.Permutation;

import java.util.Arrays;

public class Solution {
    private String sort(String str) {
        char[] contents = str.toCharArray();
        Arrays.sort(contents);
        return new String(contents);
    }

    public boolean isPermutation1(String str, String compareStr) {
        if (str.length() != compareStr.length()) {
            return false;
        }
        String sortedStr = sort(str);
        String sortedCompareStr = sort(compareStr);

        return sortedStr.equals(sortedCompareStr);
    }

    public boolean isPermutation2(String str, String compareStr) {
        if (str.length() != compareStr.length()) {
            return false;
        }

        int[] letters = new int[256];
        char[] charArray = str.toCharArray();
        for (char c : charArray) {
            letters[c]++;
        }

        for (int i = 0; i < compareStr.length(); i++) {
            int val = compareStr.charAt(i);
            if (--letters[val] < 0) {
                return false;
            }
        }
        return true;
    }

    public static void main(String[] args) {
        var s = new Solution();
        var ret = s.isPermutation1("catis", "iscat");
        System.out.println(ret);

        ret = s.isPermutation2("catis", "iscat");
        System.out.println(ret);
    }
}
