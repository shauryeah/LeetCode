# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def levelOrder(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: List[List[int]]
        """
        from collections import deque
        Queue=deque([root])
        ans=[]
        while(Queue):
            if(not root):
                return []
            level_size=len(Queue)
            lev=[]
            for i in range(level_size):
                node=Queue.popleft()
                lev.append(node.val)
                if(node.left):
                    Queue.append(node.left)
                if(node.right):
                    Queue.append(node.right)
            ans.append(lev)
        return ans


            
            
            