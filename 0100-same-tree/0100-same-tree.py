# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def isSameTree(self, p, q):
        """
        :type p: Optional[TreeNode]
        :type q: Optional[TreeNode]
        :rtype: bool
        """
        def check(t1,t2):
            if(not t1 or not t2):
                if(not t1 and t2):
                    return False
                elif(t1 and not t2): 
                    return False
                else:
                    return True
            return t1.val==t2.val and check(t1.left,t2.left) and check(t1.right,t2.right)
        return check(p,q)