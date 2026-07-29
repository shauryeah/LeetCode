# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def middleNode(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        curr=head
        count=0
        while(curr):
            curr=curr.next
            count+=1
        if(count%2==0):
            for i in range(count/2):
                head=head.next
        else:
            for i in range(count//2):
                head=head.next
        return head