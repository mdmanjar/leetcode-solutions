# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:

        def merge(l1,l2):
            head=ListNode(-1)
            temp=head

            while l1 and l2:
                if l1.val<l2.val:
                    temp.next=l1
                    l1=l1.next
                else:
                    temp.next=l2
                    l2=l2.next
                temp=temp.next
            temp.next=l1 or l2
            return head.next

        def divid(head):
            if head is None or head.next is None:return head

            slow=fast=head

            while fast and fast.next and fast.next.next:
                slow=slow.next
                fast=fast.next.next
            nxt=slow.next
            slow.next=None

            return merge(divid(head),divid(nxt))
        return divid(head)
        