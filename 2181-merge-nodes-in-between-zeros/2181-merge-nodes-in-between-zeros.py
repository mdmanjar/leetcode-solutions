# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
      dummy=ListNode(-1)
      temp=dummy
      sm=0

      while head:
        if head.val==0:
            if sm!=0:
                temp.next=ListNode(sm)
                temp=temp.next
            sm=0
        sm+=head.val
        head=head.next
      return dummy.next
        