package Cracking_the_Coding_Interview.DataStructure.ArrayAndString.Permutation;

import java.util.Arrays;

public class Solution {
    private String sort(String str) {
        char[] contents = str.toCharArray();
        Arrays.sort(contents);
        return new String(contents);
    }

    public boolean isPermutation(String str, String compareStr) {
        String sortedStr = sort(str);
        String sortedCompareStr = sort(compareStr);

        return sortedStr.equals(sortedCompareStr);
    }

    public static void main(String[] args) {
        var s = new Solution();
        var ret = s.isPermutation("catis", "iscat");
        System.out.println(ret);
    }
}
