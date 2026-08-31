# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def nodesBetweenCriticalPoints(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: List[int]
        """
        cnt=1
        first=-1
        last=-1
        mindis=float('inf')
        prev=head
        curr=head.next
        while(curr.next):
            if((curr.val<prev.val and curr.val<curr.next.val) or (curr.val>prev.val and curr.val>curr.next.val)):
                if(first==-1):
                    first=cnt
                else:
                    mindis=min(mindis,cnt-last)
                last=cnt
            prev=curr
            curr=curr.next
            cnt+=1
        if first==-1 or first==last:
            return [-1,-1]
        return [mindis,last-first]