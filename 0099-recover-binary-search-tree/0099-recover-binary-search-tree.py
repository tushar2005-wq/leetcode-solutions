# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def recoverTree(self, root):
        inorder_nodes=[]
        def inorder(node):
            if not node:
                return
            inorder(node.left)

            inorder_nodes.append(node)

            inorder(node.right)
        inorder(root)
        values=[node.val for node in inorder_nodes]
        sorted_values=sorted(values)

        first=None
        second=None
        for i in range(len(values)):
            if values[i]!=sorted_values[i]:
                if not first:
                    first=inorder_nodes[i]
                else:
                    second=inorder_nodes[i]
        first.val,second.val=second.val,first.val
        
            
        """
        :type root: Optional[TreeNode]
        :rtype: None Do not return anything, modify root in-place instead.
        """
        