package Two_Sum;

import java.util.HashMap;
import java.util.Map;

class Solution {
    public int[] twoSum(int[] nums, int target) {
        Map<Integer, Integer> map = new HashMap<>();

        for (int i = 0; i < nums.length; i++) {
            int cur = nums[i];
            if (map.containsKey(target - cur)) {
                int[] ret = new int[2];
                ret[0] = map.get(target - cur);
                ret[1] = i;

                return ret;
            } else {
                map.put(cur, i);
            }
        }
        return null;
    }
}