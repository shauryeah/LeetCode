# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def diameterOfBinaryTree(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: int
        """
        ans=[0]
        def furth(node):
            if(not node):
                return 0
            lheight=furth(node.left)
            rheight=furth(node.right)
            ans[0]=max(ans[0],lheight+rheight)
            return 1+max(lheight,rheight)
        furth(root)
        return ans[0]