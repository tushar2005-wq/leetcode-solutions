# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def isBalanced(self, root):
        if not root:
            return True
        def depth(node):
            if not node:
                return 0
            left_depth=depth(node.left)
            right_depth=depth(node.right)
            return 1+max(left_depth,right_depth)
        left_ht=depth(root.left)
        right_ht=depth(root.right)
        if abs(left_ht-right_ht)>1:
            return False
        return self.isBalanced(root.left) and self.isBalanced(root.right)
        """
        :type root: Optional[TreeNode]
        :rtype: bool
        """
        