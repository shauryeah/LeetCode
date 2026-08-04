# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def maxDepth(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: int
        """
        def rec(node):
            if(not node):
                return 0
            left_height=rec(node.left)
            right_height=rec(node.right)
            return 1+max(left_height,right_height)
        return rec(root)
            