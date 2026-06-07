# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def rotateRight(self, head, k):
        """
        :type head: Optional[ListNode]
        :type k: int
        :rtype: Optional[ListNode]
        """
        if(not head):
            return head
        if(not head.next):
            return head
        length=0
        curr=head
        while(curr):
            length+=1
            curr=curr.next
        k=k%length
        
        for i in range(k):
            curr1=head
            curr2=head
            while(curr1.next.next):
                curr1=curr1.next
            curr1.next.next=curr2
            head=curr1.next
            curr1.next=None
        return head


