# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: Optional[ListNode]
        :type l2: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        l3=ListNode(0)
        dummy=l3
        carry=0
        while(l1 or l2 or carry):
            if(not l1):
                val1=0
            else:
                val1=l1.val
            if(not l2):
                val2=0
            else:
                val2=l2.val
            summ=val1+val2+carry
            carry=summ//10
            digit=summ%10
            l3.next=ListNode(digit)
            l3=l3.next
            if(l1):
                l1=l1.next
            if(l2):
                l2=l2.next
        return dummy.next
            


