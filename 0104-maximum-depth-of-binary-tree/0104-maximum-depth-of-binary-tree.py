from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def maxDepth(self, root: Optional[TreeNode], result: int = 0) -> int:
        if root is None:
            return result

        return max(self.maxDepth(root.left, result+1), self.maxDepth(root.right, result+1))
