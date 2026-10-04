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
        last=None

        def dfs(head):
            nonlocal last
            while head and not head.child:
                last=head
                head=head.next
            if head is None:return
            last=head
            child=head.child
            head.child=None
            next=head.next
            child.prev=head
            head.next=child
            dfs(head)
            if next is None:return
            last.next=next
            next.prev=last
            dfs(last)
        dfs(head)
        return head
        