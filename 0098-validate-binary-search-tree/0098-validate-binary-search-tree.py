from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def is_valid(node: Optional[TreeNode], low: float, high: float) -> bool:
            if not node:
                return True
            if not (node.val < high and node.val > low):
                return False
            
            return (is_valid(node.left, low, node.val) and is_valid(node.right, node.val, high))
        
        return is_valid(root, float("-inf"), float("inf"))
