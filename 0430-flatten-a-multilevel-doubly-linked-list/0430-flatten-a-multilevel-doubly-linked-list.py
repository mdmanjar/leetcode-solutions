"""
# Definition for a Node.
class Node:
    def __init__(self, val, prev, next, child):
        self.val = val
        self.prev = prev
        self.next = next
        self.child = child
"""

class Solution:
    def flatten(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if head is None:return head
        last=None

        def dfs(head):
            nonlocal last
            while head and not head.child:
                last=head
                head=head.next
            if not head:return
            last=head
            nxt=head.next
            head.next=head.child
            head.child.prev=head
            head.child=None
            dfs(head)
            if nxt is None:return

            last.next=nxt
            nxt.prev=last
            dfs(last)
        dfs(head)
        return head




        