# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def isBalanced(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: bool
        """
        def height(node):
            if(not node):
                return 0
            lheight=height(node.left)
            rheight=height(node.right)
            if lheight==-1:
                return -1
            if rheight==-1:
                return -1   
            if(abs(lheight-rheight)<=1):
                return 1+max(lheight,rheight)
            else:
                return -1
        return height(root)!=-1
        
