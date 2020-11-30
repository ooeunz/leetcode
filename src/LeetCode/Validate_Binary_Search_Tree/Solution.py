class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def check_valid(self, node: TreeNode, lower=float('-inf'), upper=float('inf')):
        if node is None:
            return True
        if lower < node.val < upper:
            return self.check_valid(node.left, lower, node.val) and self.check_valid(node.right, node.val, upper)
        else:
            return False

    def isValidBST(self, root: TreeNode) -> bool:
        return self.check_valid(root)
