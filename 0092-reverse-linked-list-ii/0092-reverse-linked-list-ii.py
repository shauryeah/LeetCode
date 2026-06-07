# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def reverseBetween(self, head, left, right):
        """
        :type head: Optional[ListNode]
        :type left: int
        :type right: int
        :rtype: Optional[ListNode]
        """
        dummy=ListNode(0)
        dummy.next=head
        curr1=head
        temp1=dummy
        for i in range(left-1):
            if(curr1.next):
                temp1=temp1.next
        curr1=temp1.next
        for i in range(right-left):
            move=curr1.next
            curr1.next=move.next
            move.next=temp1.next
            temp1.next=move
        return dummy.next
        