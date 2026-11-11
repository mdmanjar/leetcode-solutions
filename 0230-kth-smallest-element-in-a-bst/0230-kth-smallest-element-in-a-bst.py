# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: TreeNode | None, k: int) -> int:
        ans=None

        def dfs(root):
            nonlocal ans,k
            if root is None:return
            dfs(root.left)
            if k==1:
                ans=root.val
            k-=1
            if ans is None:
                dfs(root.right)
        dfs(root)
        return ans
        