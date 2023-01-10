package leetcode.Flatten_Binary_Tree_to_Linked_List;

import java.util.ArrayList;
import java.util.List;

public class Solution {
    public void flatten(TreeNode root) {
        if (root == null) {
            return;
        }
        List<Integer> arr = new ArrayList<>();
        dfs(arr, root);
        for (int i = 1; i < arr.size(); i++) {
            int val = arr.get(i);
            root.right = new TreeNode(val);
            root = root.right;
        }
    }

    public void dfs(List<Integer> arr, TreeNode node) {
        arr.add(node.val);

        if (node.left != null) {
            dfs(arr, node.left);
            node.left = null;
        }
        if (node.right != null) {
            dfs(arr, node.right);
            node.right = null;
        }
    }
}