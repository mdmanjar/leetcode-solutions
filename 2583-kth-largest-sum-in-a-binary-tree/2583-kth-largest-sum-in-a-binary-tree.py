# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthLargestLevelSum(self, root: TreeNode | None, k: int) -> int:
        hp=[]
        q=deque([root])

        while q:
            sm=0
            for _ in range(len(q)):
                cur=q.popleft()
                sm+=cur.val
                if cur.left:q.append(cur.left)
                if cur.right:q.append(cur.right)

            heapq.heappush(hp,sm)
            if len(hp)>k:heapq.heappop(hp)

        return hp[0] if len(hp)==k else -1
        