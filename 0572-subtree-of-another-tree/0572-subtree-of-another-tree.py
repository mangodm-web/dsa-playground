from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        if not subRoot:
            return True
        if not root:
            return False
        
        if self.isSameTree(root, subRoot):
            return True
        
        has_subroot_in_left = self.isSubtree(root.left, subRoot)
        has_subroot_in_right = self.isSubtree(root.right, subRoot)

        return has_subroot_in_left or has_subroot_in_right

    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        if not p and not q:
            return True
        
        if p and q and p.val == q.val:
            is_left_equal = self.isSameTree(p.left, q.left)
            is_right_equal = self.isSameTree(p.right, q.right)

            return is_left_equal and is_right_equal
        
        return False
