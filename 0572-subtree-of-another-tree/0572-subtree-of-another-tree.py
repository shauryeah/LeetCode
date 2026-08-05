# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def isSubtree(self, root, subRoot):
        """
        :type root: Optional[TreeNode]
        :type subRoot: Optional[TreeNode]
        :rtype: bool
        """
        def same(root1,root2):
            if (not root1 or not root2):
                if(not root1 and not root2):
                    return True
                else:
                    return False
            return root1.val==root2.val and same(root1.left,root2.left) and same(root1.right,root2.right)
        def sub(root,subroot):
            if(same(root,subroot)):
                return True
            if(not root):
                return False
            return sub(root.left,subroot) or sub(root.right,subroot)
        return sub(root,subRoot)