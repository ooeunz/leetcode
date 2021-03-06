package Cracking_the_Coding_Interview.DataStructure.ArrayAndString.NoOverlap;

public class Solution {
    public boolean isUniqueChars(String s) {
        if (s.length() > 127) {
            return false;
        }
        boolean[] charSet = new boolean[128];
        for (int i = 0; i < s.length(); i++) {
            int asciiCode = s.charAt(i);
            if (charSet[asciiCode]) {
                return false;
            }
            charSet[asciiCode] = true;
        }
        return true;
    }

    public static void main(String[] args) {
        Solution solution = new Solution();
        System.out.println(solution.isUniqueChars("adsf"));
        System.out.println(!solution.isUniqueChars("aa"));
    }
}
