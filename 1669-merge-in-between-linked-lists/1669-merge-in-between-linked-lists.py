# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeInBetween(self, list1: ListNode, a: int, b: int, list2: ListNode) -> ListNode:
        list1=ListNode(-1,list1)
        t=list1

        while t and a:
            t=t.next
            a-=1
            b-=1
        nxt=t.next
        t.next=list2

        while t.next:
            t=t.next
        while nxt and b:
            nxt=nxt.next
            b-=1
        t.next=nxt.next
        return list1.next
        