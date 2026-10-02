# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def spiralMatrix(self, m: int, n: int, head: Optional[ListNode]) -> List[List[int]]:
        ans=[[-1]*n for _ in range(m)]

        dirs=((0,1),(1,0),(0,-1),(-1,0))
        didx=0

        def next(idx,i,j):

            u=i+dirs[idx][0]
            v=j+dirs[idx][1]

            if not (-1<u<m and -1<v<n and ans[u][v]==-1):
                return (idx+1)%4

            return idx

        i=j=0


        while head:
            ans[i][j]=head.val
            head=head.next
            didx=next(didx,i,j)
            i+=dirs[didx][0]
            j+=dirs[didx][1]

        return ans
        