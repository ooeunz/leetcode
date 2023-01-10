package leetcode.Median_of_Two_Sorted_Arrays;

import java.util.ArrayList;
import java.util.List;

class Solution {
    public double findMedianSortedArrays(int[] nums1, int[] nums2) {
        int nm1 = 0;
        int nm2 = 0;

        List<Integer> ans = new ArrayList<>();
        while (nm1 < nums1.length && nm2 < nums2.length) {
            if (nums1[nm1] < nums2[nm2]) {
                ans.add(nums1[nm1++]);
            } else {
                ans.add(nums2[nm2++]);
            }
        }

        if (nm1 < nums1.length) {
            while (nm1 < nums1.length) {
                ans.add(nums1[nm1++]);
            }
        } else {
            while (nm2 < nums2.length) {
                ans.add(nums2[nm2++]);
            }
        }

        int mid = ans.size() / 2;
        if (ans.size() % 2 == 0) {
            return (float) (ans.get(mid - 1) + ans.get(mid)) / 2;
        }
        return ans.get(mid);
    }

    public static void main(String[] args) {
        Solution solution = new Solution();

        int[] nums1 = {1, 3};
        int[] nums2 = {2};
        System.out.println(solution.findMedianSortedArrays(nums1, nums2) == 2.0);

        nums1 = new int[]{1, 2};
        nums2 = new int[]{3, 4};
        System.out.println(solution.findMedianSortedArrays(nums1, nums2) == 2.5);
    }
}