# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def postorderTraversal(self, root):
        if not root:
            return []
        output=[]
        if root.left:
            output+=self.postorderTraversal(root.left)
        if root.right:
            output+=self.postorderTraversal(root.right)
        output.append(root.val)
        return output
        """
        :type root: Optional[TreeNode]
        :rtype: List[int]
        """
        