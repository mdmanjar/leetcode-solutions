# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: list[ListNode | None]) -> ListNode | None:
        if lists is None:return None
        
        def merge(l1,l2):
            head=ListNode()
            temp=head

            while l1 and l2 :
                if l1.val<l2.val:
                    temp.next=l1
                    l1=l1.next
                else:
                    temp.next=l2
                    l2=l2.next
                
                temp=temp.next
            temp.next=l1 or l2
            return head.next


        def divide(left,right):
            if left>right:return  None
            if left==right:return lists[left]
            mid=left+(right-left)//2
            return merge(divide(left,mid),divide(mid+1,right))
        return divide(0,len(lists)-1)
        
        