class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def find_depth(self, node: TreeNode, depth: int):
        if node is None:
            return depth
        return max(self.find_depth(node.left, depth + 1), self.find_depth(node.right, depth + 1))

    def maxDepth(self, root: TreeNode) -> int:
        return self.find_depth(root, 0)
