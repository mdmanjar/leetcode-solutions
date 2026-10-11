# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def sortList(self, head: ListNode | None) -> ListNode | None:

        def sort(head):
            if head is None or head.next is None:
                return head
            slow=fast=head

            while fast and fast.next and fast.next.next:
                slow=slow.next
                fast=fast.next.next

            next=slow.next
            slow.next=None

            head=sort(head)
            next=sort(next)
            temp=ListNode()
            new_head=temp

            while head and next:
                if head.val<next.val:
                    temp.next=head
                    head=head.next
                else:
                    temp.next=next
                    next=next.next
                temp=temp.next
            temp.next=head or next
            
            return new_head.next
        return sort(head)
            
        