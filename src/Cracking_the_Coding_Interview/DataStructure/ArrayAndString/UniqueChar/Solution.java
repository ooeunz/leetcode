package Cracking_the_Coding_Interview.DataStructure.ArrayAndString.UniqueChar;

public class Solution {
    public boolean isUniqueChars2(String str) {
        if (str.length() > 256) {
            return false;
        }
        boolean[] charSet = new boolean[256];
        for (int i = 0; i < str.length(); i++) {
            int val = str.charAt(i);
            if (charSet[val]) {
                return false;
            }
            charSet[val] = true;
        }
        return true;
    }

    public boolean isUniqueChar(String str) {
        if (str.length() > 26) {
            return false;
        }
        int checker = 0;
        for (int i = 0; i < str.length(); i++) {
            int val = str.charAt(i) - 'a';
            if ((checker & (1 << val)) > 0) {
                return false;
            }
            checker |= (1 << val);
        }
        return true;
    }

    public static void main(String[] args) {
        var s = new Solution();

        var ret = s.isUniqueChars2("asdf");
        System.out.println(ret);

        ret = s.isUniqueChar("asdfg");
        System.out.println(ret);
    }
}
