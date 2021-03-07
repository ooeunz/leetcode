# [Flatten Binary Tree to Linked List](https://leetcode.com/problems/flatten-binary-tree-to-linked-list/)

Binary Tree가 주어졌을 경우, Tree를 flat하게 펴주는 문제입니다.

### solve 1.
dfs 알고리즘으로 모든 노드를 순환하며 순서대로 List에 값을 담아줍니다.
그런 다음 root부터 right 방향으로 하나씩 List에 들어있는 값을 추가해줍니다.

```java
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
```