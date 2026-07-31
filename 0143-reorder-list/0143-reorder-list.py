# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def reorderList(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: None Do not return anything, modify head in-place instead.
        """
        fast=head
        slow=head
        prev=None
        prevtoslow=ListNode(0)
        prevtoslow.next=slow
        while fast and fast.next:
            fast=fast.next.next
            slow=slow.next
            prevtoslow=prevtoslow.next
        slow=slow.next
        prevtoslow=prevtoslow.next
        prevtoslow.next=None
        while(slow):
            temp=slow.next
            slow.next=prev
            prev=slow
            slow=temp
        curr=head
        while(prev and curr):
            temp1=prev.next
            temp2=curr.next
            curr.next=prev
            prev.next=temp2
            curr=temp2
            prev=temp1
        return head
