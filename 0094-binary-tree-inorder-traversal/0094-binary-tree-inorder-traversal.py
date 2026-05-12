# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def inorderTraversal(self, root):

        elements=[]
        if not root:
            return []
        if root.left:
            elements+=self.inorderTraversal(root.left)
        elements.append(root.val)
        if root.right:
            elements+=self.inorderTraversal(root.right)
        return elements
        """
        :type root: Optional[TreeNode]
        :rtype: List[int]
        """
        