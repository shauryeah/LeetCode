# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def isSymmetric(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: bool
        """
        def check(left,right):
            if(not left or not right):
                if(not left and right):
                    return False
                elif(not right and left):
                    return False
                else:
                    return True
            
            return left.val==right.val and check(left.left,right.right) and check(left.right,right.left)
            
        return check(root.left,root.right)  