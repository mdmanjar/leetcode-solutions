# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: list[ListNode | None]) -> ListNode | None:
        if not lists:return None

        offset=10000
        mp=[0]*20001

        for x in lists:
            while x:
                mp[x.val+offset]+=1
                x=x.next

        head=ListNode(-1)
        temp=head

        for i in range(len(mp)):
            while mp[i]:
                temp.next=ListNode(i-offset)
                temp=temp.next
                mp[i]-=1

        return head.next