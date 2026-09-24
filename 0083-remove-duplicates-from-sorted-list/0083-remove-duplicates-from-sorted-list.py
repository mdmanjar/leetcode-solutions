# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy=ListNode(inf)
        temp=dummy

        while head:
            if temp.val!=head.val:
                temp.next=head
                temp=temp.next
            head=head.next
        temp.next=None
        return dummy.next

        