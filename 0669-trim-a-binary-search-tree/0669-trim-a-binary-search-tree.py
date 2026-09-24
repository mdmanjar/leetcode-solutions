# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def trimBST(self, root: Optional[TreeNode], low: int, high: int) -> Optional[TreeNode]:

        def dfs(r):
            if r is None:
                return None
            if r.val<low:
                return dfs(r.right)
            if r.val>high:
                return dfs(r.left)
            r.left=dfs(r.left)
            r.right=dfs(r.right)
            return r


        return dfs(root)
        