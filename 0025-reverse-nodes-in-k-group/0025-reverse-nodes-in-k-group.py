# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:

        def reverse(head):
            prev=None

            while head:
                nxt=head.next
                head.next=prev
                prev=head
                head=nxt

            return prev
        
        def dfs(head):
            if head is None or head.next is None:return head

            cnt=k
            temp=head

            while cnt>1 and temp:
                temp=temp.next
                cnt-=1

            if temp is None:return head

            nxt=temp.next
            temp.next=None

            rev=reverse(head)
            head.next=dfs(nxt)

            return rev

        return dfs(head)


