# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution(object):
    def zigzagLevelOrder(self, root):
        if not root:
            return []
        ans=[]
        flag=1
        q=deque([root])
        while q:
            size=len(q)
            level=[]
            for _ in range(size):
                node=q.popleft()
                level.append(node.val)
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
            if flag==-1:
                level.reverse()
                
            ans.append(level)
            flag=-flag
        return ans
        """
        :type root: Optional[TreeNode]
        :rtype: List[List[int]]
        """
        